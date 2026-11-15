# UI/UX, Visual Design & Lighting Skills

A self-contained collection of **142 agent skills**, **6 specialist agents** (`agents/`), and **3 zero-dependency Python CLI tools** (`tools/`) for **UI/UX design**, **design systems & visual craft**, **3D/Three.js lighting, materials & shaders**, **motion & data visualization**, and **AI visual/media generation**. Compatible with **Google Antigravity**, **Claude Code**, **OpenAI Codex**, **Gemini CLI**, **Cursor**, **Windsurf**, and any assistant supporting `AGENTS.md`.

Every skill lives as a real, standalone directory under `skills/<skill-name>/SKILL.md` (zero symlinks or junctions).

---

## Install

Copy this folder into your project or keep it in your global `~/.agents/` directory so coding agents discover `AGENTS.md`:

```bash
cp -r ui-ux-visual-lighting-skills/ my-project/.agents/
```

| Client | Entrypoint | How to Use |
|---|---|---|
| **Antigravity** | `plugin.json` + `AGENTS.md` | Place in `~/.agents/ui-ux-visual-lighting-skills/` or project workspace. |
| **Claude Code** | `.claude-plugin/plugin.json` + `CLAUDE.md` | Load with `claude --plugin-dir ~/.agents/ui-ux-visual-lighting-skills` (`CLAUDE.md` imports `@AGENTS.md`). |
| **Codex** | `.codex-plugin/plugin.json` | Register directory so Codex indexes `./skills/` and `./AGENTS.md`. |
| **Gemini CLI** | `gemini-extension.json` | Link extension (`gemini extensions link ~/.agents/ui-ux-visual-lighting-skills`). |
| **Cursor / Windsurf** | `AGENTS.md` | Reference `@AGENTS.md` or copy `AGENTS.md` + needed `skills/` into your project. |

---

## How It Works

`AGENTS.md` routes each request only to the matching domain skills so irrelevant files stay unread:

1. **Workspace Scan & Visual Brief** — Inspects `package.json`, Tailwind/CSS tokens, `DESIGN.md`, component primitives, and Three.js versions; asks only for missing aesthetic, platform, or UX constraints.
2. **Art Direction, UX & Design Tokens** — Locks visual direction (`ckw-design`, `high-end-visual-design`, `ui-ux-pro-max`), information hierarchy, and semantic tokens (`ui-tokens`, `tailwind-design-system`, `design-md`, Apple HIG).
3. **3D, Lighting & Shader Pipeline** — Builds Three.js/WebGL scenes (`threejs-scene-setup`), physically calibrated IBL + light rigs (`threejs-materials-lighting`), custom GLSL/HLSL effects (`shader-programming`, `threejs-shaders`), and post-processing (`threejs-postprocessing`).
4. **Motion, Media & Visual Verification** — Adds compositor-safe animations (`animejs-animation`, `fixing-motion-performance`), generates imagery/video/screenshots (`fal-*`, `imagen`, `remotion`, `screenshots`, `screenstudio-alt`), and validates balance, WCAG 2.2 AA contrast, and lookdev (`lookdev`, `ui-visual-validator`, `ui-a11y`, `unship`).

---

## Skills Overview (142 Skills)

| Domain | Count | Highlights |
|---|---:|---|
| **3D, Lighting, Materials, Shaders & Lookdev** | 20 | `threejs-materials-lighting`, `threejs-lighting`, `threejs-shaders`, `shader-programming`, `threejs-postprocessing`, `threejs-scene-setup`, `3d-web-experience`, `spline-3d-integration`, `lookdev`, `lookdev-auto`, `algorithmic-art` |
| **Art Direction, Visual Design & Aesthetic Systems** | 22 | `high-end-visual-design`, `ckw-design`, `frontend-design`, `design-taste-frontend`, `minimalist-ui`, `industrial-brutalist-ui`, `brand-guidelines-community`, `visual-emotion-engineer`, `premium-typography-kit`, `iconsax-library`, `product-design`, `product-inventor` |
| **UI/UX Architecture, Behavioral UX & Game UI/Feel** | 23 | `ui-ux-pro-max`, `ui-ux-designer`, `uxui-principles`, `ux-flow`, `ux-audit`, `onboarding-psychologist`, `information-hierarchy`, `structured-artifact`, `game-ui-ux`, `game-feel`, `ui-visual-validator`, `deterministic-design`, `unship` |
| **Design Systems, Tokens, Components & Accessibility** | 24 | `design-md`, `stitch-design-taste`, `figma-automation`, `shadcn`, `radix-ui-design-system`, `tailwind-design-system`, `tailwind-patterns`, `baseline-ui`, `ui-tokens`, `ui-component`, `ui-a11y`, `screen-reader-testing` |
| **Mobile & Apple HIG UI** | 19 | `mobile-design`, `building-native-ui`, `expo-tailwind-setup`, `android-jetpack-compose-expert`, `hig-foundations`, `hig-platforms`, `hig-patterns`, `hig-components-*` |
| **Motion, Animation & Data Visualization** | 9 | `animejs-animation`, `magic-animator`, `design-spells`, `scroll-experience`, `vercel-react-view-transitions`, `fixing-motion-performance`, `claude-d3js-skill`, `mermaid-expert` |
| **AI Visual, Image, Presentation & Video Media** | 25 | `image-studio`, `imagen`, `stability-ai`, `comfyui-gateway`, `fal-generate`, `fal-image-edit`, `mmx-cli`, `runapi-cli`, `vizcom`, `create-game-assets`, `nanobanana-ppt-skills`, `screenshots`, `screenstudio-alt`, `remotion`, `videodb` |

See [`AGENTS.md`](./AGENTS.md) for the complete 142-skill routing table (`Read when`).

---

## Example Prompts

### 3D Lighting, Materials & Lookdev

> Set up a Three.js r187 product showcase with HDR environment IBL, a 3-point directional/rim light rig, ACES Filmic tone mapping, and a local `lookdev` slider panel so I can tune bloom and roughness by eye.

### UI/UX Redesign & Accessibility Audit

> Scan this React + Tailwind codebase, audit the dashboard with `ux-audit` and `ui-a11y` (WCAG 2.2 AA), propose a cohesive dark-mode token palette, and let me compare two layout variants locally with `unship` before cleanup.

### Motion, Visuals & Demo Media

> Add GPU-composited route transitions and micro-interactions to our landing page (`vercel-react-view-transitions`, `design-spells`, `fixing-motion-performance`), then capture 2x HiDPI marketing screenshots (`screenshots`).

---

## CLI Tools (`tools/`) & Specialist Agents (`agents/`)

```bash
# Discover skills without flooding context
python tools/skill_catalog.py find lighting postprocessing
python tools/skill_catalog.py verify

# UI/UX, WCAG 2.2 contrast & compositor-motion checks
python tools/design_audit.py contrast "#767676" "#faf9f5"
python tools/design_audit.py a11y-scan src --strict
python tools/design_audit.py scaffold-design-md --name MyApp --style "Editorial Minimalist"

# Three.js r155+/r187 lighting, IBL, tone mapping & GLSL checks
python tools/lighting_tools.py audit-three src --strict
python tools/lighting_tools.py rig-preset studio-product --r3f
python tools/lighting_tools.py shader-check src
```

| Agent (`agents/`) | Focus |
|---|---|
| `art-director.md` | Visual direction, `DESIGN.md`, typography, palettes, anti-slop |
| `ux-architect.md` | User flows, hierarchy, microcopy, heuristic audits, onboarding |
| `design-system-engineer.md` | Tokens, `shadcn`/Radix/Tailwind/MUI/HIG components, `unship` variants |
| `lighting-shader-artist.md` | Three.js PBR, IBL, 3-point rigs, tone mapping, GLSL/HLSL, `lookdev` |
| `motion-choreographer.md` | Micro-interactions, View Transitions, scroll motion, 60fps audits |
| `visual-qa-a11y.md` | WCAG 2.2 AA, screen readers, optical balance, HiDPI QA |

---

## Layout

```text
ui-ux-visual-lighting-skills/
├── .claude-plugin/
│   └── plugin.json                  # Claude Code plugin manifest
├── .codex-plugin/
│   └── plugin.json                  # OpenAI Codex plugin manifest
├── AGENTS.md                        # Universal agent instructions, routing table & boundaries
├── CLAUDE.md                        # Claude Code entrypoint (@AGENTS.md)
├── README.md                        # Pack documentation & quick start
├── gemini-extension.json            # Gemini CLI extension manifest
├── plugin.json                      # Antigravity plugin manifest
├── agents/                          # 6 specialist agent personas
│   ├── art-director.md
│   ├── ux-architect.md
│   ├── design-system-engineer.md
│   ├── lighting-shader-artist.md
│   ├── motion-choreographer.md
│   └── visual-qa-a11y.md
├── tools/                           # Zero-dependency Python 3.8+ CLIs
│   ├── skill_catalog.py             # Skill search, inspect & pack integrity verifier
│   ├── design_audit.py              # WCAG 2.2 contrast, tokens, a11y/motion lint, DESIGN.md scaffold
│   └── lighting_tools.py            # Three.js r155+/r187 audit, lighting presets, GLSL check
└── skills/
    ├── 3d-web-experience/SKILL.md
    ├── threejs-materials-lighting/SKILL.md
    ├── shader-programming/SKILL.md
    ├── high-end-visual-design/SKILL.md
    ├── ui-ux-pro-max/SKILL.md
    ├── lookdev/SKILL.md
    └── ... (142 self-contained skill directories)
```
