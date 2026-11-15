"""3D, Three.js Lighting & Shader CLI: scene/material/r155+ audit, lighting rig presets, GLSL lint."""
import argparse
import json
import os
import re
import sys

SKIP_DIRS = {"node_modules", ".git", ".next", "dist", "build", "out", "__pycache__", ".venv"}
JS_EXT = (".js", ".jsx", ".ts", ".tsx", ".mjs", ".mts", ".html")
SHADER_EXT = (".glsl", ".vert", ".frag", ".vs", ".fs", ".wgsl")


def _walk_files(root_dir, exts):
    if os.path.isfile(root_dir):
        yield root_dir
        return
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if fn.endswith(exts):
                yield os.path.join(dirpath, fn)


def _detect_three_version(root_dir):
    pkg = os.path.join(root_dir if os.path.isdir(root_dir) else os.path.dirname(root_dir), "package.json")
    if not os.path.isfile(pkg):
        return None
    try:
        data = json.load(open(pkg, encoding="utf-8"))
        for sec in ("dependencies", "devDependencies", "peerDependencies"):
            ver = data.get(sec, {}).get("three")
            if ver:
                return ver
    except Exception:
        return None
    return None


def cmd_audit_three(args):
    if not os.path.exists(args.dir):
        sys.exit(f"[ERR] Path not found: {args.dir}")

    ver = _detect_three_version(args.dir)
    if ver:
        print(f"Detected Three.js package version: {ver}")

    findings = []
    uses_three = False
    has_tone_mapping = False
    has_env_map = False
    has_high_metal = False
    has_shadow_cast = False
    has_shadow_bias = False
    has_dispose = False

    for path in _walk_files(args.dir, JS_EXT):
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue

        if "three" not in text and "THREE." not in text:
            continue
        uses_three = True

        if "toneMapping" in text:
            has_tone_mapping = True
        if "scene.environment" in text or "envMap" in text or "PMREMGenerator" in text or "<Environment" in text:
            has_env_map = True
        if "shadow.bias" in text or "shadowBias" in text or "shadow-bias" in text:
            has_shadow_bias = True
        if "castShadow" in text:
            has_shadow_cast = True
        if ".dispose(" in text:
            has_dispose = True

        for idx, line in enumerate(text.splitlines(), 1):
            if "sRGBEncoding" in line or "outputEncoding" in line:
                findings.append(("THREE-LEGACY", path, idx, "Legacy encoding API (use renderer.outputColorSpace = THREE.SRGBColorSpace in r152+)"))
            if "physicallyCorrectLights" in line:
                findings.append(("THREE-LEGACY", path, idx, "physicallyCorrectLights removed in r155+ (physically based lighting is default)"))
            m_metal = re.search(r"metalness\s*:\s*([0-9.]+)", line)
            if m_metal and float(m_metal.group(1)) >= 0.5:
                has_high_metal = True
            m_int = re.search(r"(?:DirectionalLight|SpotLight|PointLight)\([^)]*,\s*([0-9.]+)\s*\)", line)
            if m_int and float(m_int.group(1)) <= 1.0:
                findings.append(("THREE-LIGHT", path, idx, f"Low light intensity ({m_int.group(1)}) — r155+ physical units often require 2.0-5.0+ or calibrated IBL"))

    if not uses_three:
        print("[INFO] No Three.js usage detected in target path.")
        return

    if not has_tone_mapping:
        findings.append(("THREE-TONE", args.dir, 0, "No toneMapping detected (recommend THREE.ACESFilmicToneMapping + toneMappingExposure)"))
    if has_high_metal and not has_env_map:
        findings.append(("THREE-IBL", args.dir, 0, "High metalness (>=0.5) detected without scene.environment/envMap (metallic surfaces will render dark/black)"))
    if has_shadow_cast and not has_shadow_bias:
        findings.append(("THREE-SHADOW", args.dir, 0, "castShadow enabled without shadow.bias / shadow.normalBias (risk of shadow acne)"))
    if not has_dispose:
        findings.append(("THREE-MEM", args.dir, 0, "No .dispose() calls found (ensure geometry/material/texture/renderer cleanup on unmount)"))

    if not findings:
        print("[OK] Three.js scene & lighting checks passed.")
        return

    print(f"Findings ({len(findings)}):")
    for code, path, ln, msg in findings[:50]:
        loc = f"{path}:{ln}" if ln else path
        print(f"  [{code}] {loc} — {msg}")
    if args.strict:
        sys.exit(1)


PRESETS = {
    "studio-product": {
        "desc": "Crisp 3-point studio product showcase with RoomEnvironment IBL and ACES Filmic tone mapping.",
        "toneMapping": "ACESFilmicToneMapping",
        "exposure": 1.05,
        "envIntensity": 0.85,
        "lights": [
            ("HemisphereLight", "#f5f7ff", "#26242b", 0.6, None),
            ("DirectionalLight (Key)", "#fff6eb", None, 2.8, (4, 6, 5)),
            ("DirectionalLight (Rim)", "#9cc2ff", None, 1.4, (-5, 3, -4)),
        ],
    },
    "dramatic-rim": {
        "desc": "High-contrast dark lookdev rig with cool fill and warm rim separation.",
        "toneMapping": "ACESFilmicToneMapping",
        "exposure": 1.15,
        "envIntensity": 0.45,
        "lights": [
            ("HemisphereLight", "#5e7499", "#121016", 0.35, None),
            ("DirectionalLight (Key)", "#ffd9b3", None, 3.6, (5, 7, 3)),
            ("DirectionalLight (Back Rim)", "#60a5fa", None, 2.4, (-4, 4, -6)),
        ],
    },
    "daylight-outdoor": {
        "desc": "Natural sun + sky bounce outdoor lighting rig with PCFSoftShadowMap.",
        "toneMapping": "ACESFilmicToneMapping",
        "exposure": 1.0,
        "envIntensity": 1.0,
        "lights": [
            ("HemisphereLight", "#bfe0ff", "#4d453a", 0.9, None),
            ("DirectionalLight (Sun)", "#fff4dc", None, 3.2, (10, 16, 8)),
        ],
    },
    "neon-dark": {
        "desc": "Cyber/telemetry dark scene tuned for emissive bloom and specular rim highlights.",
        "toneMapping": "ACESFilmicToneMapping",
        "exposure": 1.1,
        "envIntensity": 0.35,
        "lights": [
            ("HemisphereLight", "#3b4261", "#090a0f", 0.3, None),
            ("PointLight (Cyan Accent)", "#22d3ee", None, 8.0, (-3, 2.5, 3)),
            ("PointLight (Magenta Rim)", "#f472b6", None, 6.0, (3, 2.0, -3)),
        ],
    },
}


def cmd_rig_preset(args):
    p = PRESETS[args.preset]
    print(f"// Preset: {args.preset} — {p['desc']}\n")
    if args.r3f:
        print(f'<Canvas shadows gl={{{{ toneMapping: THREE.{p["toneMapping"]}, toneMappingExposure: {p["exposure"]} }}}}>')
        print(f'  <Environment preset="studio" environmentIntensity={{{p["envIntensity"]}}} />')
        for kind, c1, c2, inten, pos in p["lights"]:
            if kind == "HemisphereLight":
                print(f'  <hemisphereLight args={{["{c1}", "{c2}", {inten}]}} />')
            elif "PointLight" in kind:
                print(f'  <pointLight color="{c1}" intensity={{{inten}}} position={{{list(pos)}}} decay={{2}} />')
            else:
                print(f'  <directionalLight color="{c1}" intensity={{{inten}}} position={{{list(pos)}}} castShadow shadow-bias={{-0.0005}} shadow-normalBias={{0.02}} />')
        print("</Canvas>")
        return

    print(f"renderer.outputColorSpace = THREE.SRGBColorSpace;")
    print(f"renderer.toneMapping = THREE.{p['toneMapping']};")
    print(f"renderer.toneMappingExposure = {p['exposure']};")
    print("renderer.shadowMap.enabled = true;")
    print("renderer.shadowMap.type = THREE.PCFSoftShadowMap;\n")
    print("const pmrem = new THREE.PMREMGenerator(renderer);")
    print("scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;")
    print(f"scene.environmentIntensity = {p['envIntensity']};\n")
    for idx, (kind, c1, c2, inten, pos) in enumerate(p["lights"], 1):
        var = f"light{idx}"
        if kind == "HemisphereLight":
            print(f"const {var} = new THREE.HemisphereLight('{c1}', '{c2}', {inten});")
        elif "PointLight" in kind:
            print(f"const {var} = new THREE.PointLight('{c1}', {inten}, 20, 2);")
            print(f"{var}.position.set({pos[0]}, {pos[1]}, {pos[2]});")
        else:
            print(f"const {var} = new THREE.DirectionalLight('{c1}', {inten}); // {kind}")
            print(f"{var}.position.set({pos[0]}, {pos[1]}, {pos[2]});")
            print(f"{var}.castShadow = true;")
            print(f"{var}.shadow.mapSize.set(2048, 2048);")
            print(f"{var}.shadow.bias = -0.0005;")
            print(f"{var}.shadow.normalBias = 0.02;")
        print(f"scene.add({var});")


def cmd_shader_check(args):
    if not os.path.exists(args.dir):
        sys.exit(f"[ERR] Path not found: {args.dir}")

    findings = []
    scanned = 0
    for path in _walk_files(args.dir, SHADER_EXT):
        scanned += 1
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        lines = text.splitlines()
        if path.endswith((".frag", ".fs")) and "precision " not in text and "#version 3" not in text:
            findings.append(("GLSL-PREC", path, 0, "Fragment shader missing precision qualifier (e.g. precision mediump float;)"))
        for idx, line in enumerate(lines, 1):
            if re.search(r"\bpow\s*\(\s*dot\s*\(", line) and "max(" not in line:
                findings.append(("GLSL-NAN", path, idx, "pow(dot(...), exp) without max(..., 0.0) can produce NaN on negative dot products"))
            if "normalize(" in line and "0.000" not in line and "length(" not in text:
                pass  # non-blocking unless zero-length vector suspected

    if scanned == 0:
        print(f"[INFO] No standalone shader files ({', '.join(SHADER_EXT)}) found in {args.dir}.")
        return
    if not findings:
        print(f"[OK] Checked {scanned} shader file(s); no traps found.")
        return

    print(f"Shader findings ({len(findings)} across {scanned} files):")
    for code, path, ln, msg in findings:
        loc = f"{path}:{ln}" if ln else path
        print(f"  [{code}] {loc} — {msg}")
    if args.strict:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description="3D, Three.js lighting & shader CLI tools.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_aud = sub.add_parser("audit-three", help="Audit Three.js lighting, PBR materials, tone mapping & disposal")
    p_aud.add_argument("dir", nargs="?", default=".", help="Directory or file to scan")
    p_aud.add_argument("--strict", action="store_true", help="Exit 1 when issues are found")
    p_aud.set_defaults(func=cmd_audit_three)

    p_rig = sub.add_parser("rig-preset", help="Print calibrated Three.js r155+/r187 lighting rig preset")
    p_rig.add_argument("preset", choices=sorted(PRESETS.keys()), help="Lighting preset name")
    p_rig.add_argument("--r3f", action="store_true", help="Emit React Three Fiber JSX instead of vanilla Three.js")
    p_rig.set_defaults(func=cmd_rig_preset)

    p_sh = sub.add_parser("shader-check", help="Static GLSL/WGSL trap checker")
    p_sh.add_argument("dir", nargs="?", default=".", help="Directory or shader file to check")
    p_sh.add_argument("--strict", action="store_true", help="Exit 1 when issues are found")
    p_sh.set_defaults(func=cmd_shader_check)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
