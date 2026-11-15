"""UI/UX & Design System CLI: WCAG 2.2 contrast, token scan, static a11y/motion audit, and DESIGN.md scaffold."""
import argparse
import json
import os
import re
import sys

SKIP_DIRS = {
    "node_modules", ".git", ".next", "dist", "build", "out",
    "coverage", "__pycache__", ".venv", "venv", ".turbo",
}
SCAN_EXT = (".html", ".htm", ".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".css", ".scss")
MARKUP_EXT = (".html", ".htm", ".tsx", ".jsx", ".vue", ".svelte")
STYLE_EXT = (".css", ".scss")


def _walk_files(root_dir, exts):
    if os.path.isfile(root_dir):
        yield root_dir
        return
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if fn.endswith(exts):
                yield os.path.join(dirpath, fn)


# ---------------------------------------------------------------- Contrast (WCAG 2.2)

def _parse_hex(color):
    h = color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"Invalid hex color: {color}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _srgb_to_linear(c):
    s = c / 255.0
    return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4


def _rel_luminance(rgb):
    r, g, b = (_srgb_to_linear(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(c1, c2):
    l1 = _rel_luminance(_parse_hex(c1))
    l2 = _rel_luminance(_parse_hex(c2))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def _suggest_fg(fg_hex, bg_hex, target=4.5):
    fg_rgb = _parse_hex(fg_hex)
    bg_lum = _rel_luminance(_parse_hex(bg_hex))
    # Decide whether lightening or darkening yields a closer pass
    candidates = []
    for direction in (-1, 1):
        for step in range(1, 256):
            factor = step / 255.0
            if direction < 0:
                cand = tuple(max(0, int(round(c * (1 - factor)))) for c in fg_rgb)
            else:
                cand = tuple(min(255, int(round(c + (255 - c) * factor))) for c in fg_rgb)
            lum = _rel_luminance(cand)
            ratio = (max(lum, bg_lum) + 0.05) / (min(lum, bg_lum) + 0.05)
            if ratio >= target:
                dist = sum(abs(a - b) for a, b in zip(fg_rgb, cand))
                candidates.append((dist, "#{:02x}{:02x}{:02x}".format(*cand), ratio))
                break
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1], candidates[0][2]


def cmd_contrast(args):
    ratio = contrast_ratio(args.fg, args.bg)
    aa_norm = ratio >= 4.5
    aa_large = ratio >= 3.0
    aaa_norm = ratio >= 7.0
    print(f"Foreground : {args.fg}")
    print(f"Background : {args.bg}")
    print(f"Ratio      : {ratio:.2f}:1")
    print(f"WCAG AA    : {'PASS' if aa_norm else 'FAIL'} (normal >= 4.5:1) | {'PASS' if aa_large else 'FAIL'} (large/UI >= 3.0:1)")
    print(f"WCAG AAA   : {'PASS' if aaa_norm else 'FAIL'} (normal >= 7.0:1)")
    if not aa_norm:
        sug = _suggest_fg(args.fg, args.bg, 4.5)
        if sug:
            print(f"Nearest AA : {sug[0]} ({sug[1]:.2f}:1)")
        if args.strict:
            sys.exit(1)


# ---------------------------------------------------------------- Tokens

CSS_VAR_RE = re.compile(r"(--[a-zA-Z0-9_-]+)\s*:\s*([^;}{]+);")
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")


def cmd_tokens(args):
    if not os.path.exists(args.dir):
        sys.exit(f"[ERR] Path not found: {args.dir}")

    css_vars = {}
    hardcoded = []
    for path in _walk_files(args.dir, SCAN_EXT):
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for idx, line in enumerate(text.splitlines(), 1):
            matches = list(CSS_VAR_RE.finditer(line))
            if matches:
                for m in matches:
                    css_vars[m.group(1)] = m.group(2).strip()
                continue
            if path.endswith(STYLE_EXT) or "style=" in line or "className=" in line:
                for hm in HEX_RE.finditer(line):
                    val = hm.group(0)
                    if len(val) in (4, 7, 9):
                        hardcoded.append((path, idx, val))

    if args.json:
        print(json.dumps({"css_variables": css_vars, "hardcoded_hex_count": len(hardcoded)}, indent=2))
        return

    print(f"CSS Custom Properties found: {len(css_vars)}")
    for k in sorted(css_vars)[:30]:
        print(f"  {k}: {css_vars[k]}")
    if len(css_vars) > 30:
        print(f"  ... and {len(css_vars) - 30} more")

    print(f"\nHardcoded hex occurrences outside var definitions: {len(hardcoded)}")
    for path, ln, val in hardcoded[:25]:
        print(f"  {path}:{ln}  {val}")
    if len(hardcoded) > 25:
        print(f"  ... and {len(hardcoded) - 25} more")


# ---------------------------------------------------------------- A11y & Motion Audit

NON_COMPOSITED = ("width", "height", "top", "left", "right", "bottom", "margin", "padding")


def cmd_a11y_scan(args):
    if not os.path.exists(args.dir):
        sys.exit(f"[ERR] Path not found: {args.dir}")

    findings = []
    has_animation = False
    has_reduced_motion = False

    for path in _walk_files(args.dir, SCAN_EXT):
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        lines = text.splitlines()

        if "prefers-reduced-motion" in text:
            has_reduced_motion = True
        if "@keyframes" in text or "animation:" in text or "animate-" in text:
            has_animation = True

        for idx, line in enumerate(lines, 1):
            if path.endswith(MARKUP_EXT):
                if re.search(r"<img\b(?![^>]*\balt=)[^>]*>", line):
                    findings.append(("A11Y-IMG", path, idx, "<img> missing alt attribute"))
                if re.search(r"<(div|span)\b[^>]*\bonClick\s*=", line) and "role=" not in line:
                    findings.append(("A11Y-BTN", path, idx, "Clickable <div>/<span> without role (prefer <button>)"))
                if re.search(r"<(input|select|textarea)\b", line) and not any(
                    k in line for k in ("aria-label", "aria-labelledby", "id=", 'type="hidden"', "type='hidden'")
                ):
                    findings.append(("A11Y-LBL", path, idx, "Form control missing id or aria-label"))
                if re.search(r'target\s*=\s*["\']_blank["\']', line) and "rel=" not in line:
                    findings.append(("UX-LINK", path, idx, 'target="_blank" missing rel="noopener noreferrer"'))

            if path.endswith(STYLE_EXT):
                if re.search(r"transition\s*:\s*all\b", line):
                    findings.append(("PERF-MOT", path, idx, "transition: all animates layout/paint properties"))
                for prop in NON_COMPOSITED:
                    if re.search(rf"transition[^;]*\b{prop}\b", line):
                        findings.append(("PERF-MOT", path, idx, f"Transitioning layout property '{prop}' (prefer transform/opacity)"))
                if re.search(r"outline\s*:\s*(none|0)\b", line) and "focus-visible" not in text:
                    findings.append(("A11Y-FOC", path, idx, "outline: none without :focus-visible replacement"))

    if has_animation and not has_reduced_motion:
        findings.append(("A11Y-MOT", args.dir, 0, "Animations detected without prefers-reduced-motion media query"))

    if not findings:
        print("[OK] No static a11y or motion issues detected.")
        return

    print(f"Findings ({len(findings)}):")
    for code, path, ln, msg in findings[:60]:
        loc = f"{path}:{ln}" if ln else path
        print(f"  [{code}] {loc} — {msg}")
    if len(findings) > 60:
        print(f"  ... and {len(findings) - 60} more")

    if args.strict:
        sys.exit(1)


# ---------------------------------------------------------------- DESIGN.md Scaffold

DESIGN_MD_TEMPLATE = """# Design System Specification — {name}

## 1. Visual Direction & Mood
- **Aesthetic:** {style}
- **Density:** Comfortable / scannable; generous negative space around primary actions.
- **Anti-Slop Rule:** No unrequested generic purple-blue gradients, stacked decorative borders, or generic placeholder copy.

## 2. Color Tokens (WCAG 2.2 AA Verified)
| Role | Light | Dark | Notes |
|---|---|---|---|
| `--bg-canvas` | `#faf9f5` | `#111214` | Primary page background |
| `--bg-surface` | `#ffffff` | `#181a1f` | Cards, panels, sheets |
| `--text-primary` | `#141413` | `#f4f4f2` | >= 4.5:1 against canvas & surface |
| `--text-muted` | `#5c5b57` | `#a1a1aa` | Secondary labels & metadata |
| `--accent-primary` | `#2563eb` | `#60a5fa` | Primary interactive CTA & focus ring |
| `--border-subtle` | `#e5e3dc` | `#272a33` | Hairline dividers |

## 3. Typography Scale
- **Display:** Expressive sans or editorial serif (`clamp(2rem, 4vw, 3.5rem)`, line-height `1.1`, tracking `-0.02em`)
- **Body:** Clean sans (`1rem` / `16px`, line-height `1.6`, max measure `68ch`)
- **Mono / Data:** Tabular numerals (`font-variant-numeric: tabular-nums`)

## 4. Spacing, Radius & Elevation
- **Scale:** 4px base (`4, 8, 12, 16, 24, 32, 48, 64, 96`)
- **Radius:** `6px` controls, `12px` cards, `9999px` pills
- **Touch Targets:** Minimum `44x44px` on touch devices

## 5. Motion & Accessibility
- **Compositor Only:** Animate only `transform` and `opacity` (150–260ms `cubic-bezier(0.22, 1, 0.36, 1)`).
- **Reduced Motion:** Wrap non-essential motion in `@media (prefers-reduced-motion: reduce)`.
- **Focus:** Visible `2px` focus-visible ring with `2px` offset.
"""


def cmd_scaffold(args):
    out_path = args.out
    if os.path.exists(out_path) and not args.force:
        sys.exit(f"[ERR] {out_path} already exists (pass --force to overwrite)")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(DESIGN_MD_TEMPLATE.format(name=args.name, style=args.style))
    print(f"[OK] Wrote {out_path}")


def main():
    ap = argparse.ArgumentParser(description="UI/UX & Design System audit and scaffold CLI.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_con = sub.add_parser("contrast", help="Compute WCAG 2.2 contrast ratio between two hex colors")
    p_con.add_argument("fg", help="Foreground hex (e.g. #141413)")
    p_con.add_argument("bg", help="Background hex (e.g. #faf9f5)")
    p_con.add_argument("--strict", action="store_true", help="Exit 1 if WCAG AA normal (4.5:1) fails")
    p_con.set_defaults(func=cmd_contrast)

    p_tok = sub.add_parser("tokens", help="Inspect CSS variables and hardcoded hex values")
    p_tok.add_argument("dir", nargs="?", default=".", help="Directory or file to scan")
    p_tok.add_argument("--json", action="store_true", help="Print JSON summary")
    p_tok.set_defaults(func=cmd_tokens)

    p_a11y = sub.add_parser("a11y-scan", help="Static accessibility & compositor-motion lint")
    p_a11y.add_argument("dir", nargs="?", default=".", help="Directory or file to scan")
    p_a11y.add_argument("--strict", action="store_true", help="Exit 1 when issues are found")
    p_a11y.set_defaults(func=cmd_a11y_scan)

    p_scaf = sub.add_parser("scaffold-design-md", help="Scaffold a DESIGN.md specification")
    p_scaf.add_argument("--name", default="App", help="Project name")
    p_scaf.add_argument("--style", default="Editorial Minimalist", help="Visual aesthetic direction")
    p_scaf.add_argument("--out", default="DESIGN.md", help="Output file path")
    p_scaf.add_argument("--force", action="store_true", help="Overwrite existing file")
    p_scaf.set_defaults(func=cmd_scaffold)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
