# UI/UX, Visual Design & Lighting Skills

Curated skill pack (**142 self-contained skills**, **6 specialist agents** in `agents/`, and **3 Python CLI tools** in `tools/`) for **UI/UX engineering**, **design systems & visual craft**, **3D/Three.js lighting, materials & shaders**, **motion**, and **AI visual/media generation**. Pick only the skills that match the task in front of you; leave the rest unread.

---

## CLI Tools (`tools/`)

Zero-dependency Python 3.8+ utilities — run these instead of guessing contrast ratios, scanning 142 `SKILL.md` files manually, or missing Three.js r155+ lighting traps:

```bash
python tools/skill_catalog.py find lighting shader            # search 142 skills by keyword
python tools/skill_catalog.py inspect threejs-materials-lighting
python tools/skill_catalog.py verify                          # verify pack parity, manifests, zero symlinks

python tools/design_audit.py contrast "#141413" "#faf9f5"     # WCAG 2.2 AA/AAA contrast + nearest passing hex
python tools/design_audit.py tokens src                       # list CSS variables & raw hardcoded hex values
python tools/design_audit.py a11y-scan src --strict           # static a11y & compositor-motion lint (exit 1 on findings)
python tools/design_audit.py scaffold-design-md --name MyApp  # scaffold DESIGN.md

python tools/lighting_tools.py audit-three src --strict       # Three.js r155+/r187 IBL, tone mapping, shadow & dispose audit
python tools/lighting_tools.py rig-preset studio-product      # calibrated lighting rig (--r3f for React Three Fiber)
python tools/lighting_tools.py shader-check src --strict      # GLSL/WGSL precision & NaN trap checker
```

## Specialist Agents (`agents/`)

| Agent | Role |
|---|---|
| `agents/art-director.md` | Visual direction, `DESIGN.md`, color/typography hierarchy, brand alignment, anti-slop gates. |
| `agents/ux-architect.md` | Information hierarchy, user flows, onboarding, microcopy, heuristic audits, game HUD/UX. |
| `agents/design-system-engineer.md` | Design tokens, Tailwind/`shadcn`/Radix/MUI/HIG components, and `unship` local variant comparison. |
| `agents/lighting-shader-artist.md` | 3D scenes, Three.js r187 PBR materials, IBL/3-point rigs, tone mapping, GLSL/HLSL shaders, `lookdev`. |
| `agents/motion-choreographer.md` | Micro-interactions, GSAP/Anime/View Transitions, scroll storytelling, `game-feel`, compositor-only motion. |
| `agents/visual-qa-a11y.md` | WCAG 2.2 AA contrast & screen-reader checks, deterministic layout audits, HiDPI screenshot/demo QA. |

---

## Skills by Domain

### 1. 3D, Lighting, Materials, Shaders & Lookdev (20)

| Skill | Read when |
|---|---|
| `skills/3d-web-experience/SKILL.md` | Building interactive 3D web experiences, scroll-driven 3D product showcases, or WebGL hero scenes. |
| `skills/threejs-skills/SKILL.md` | Entry point for Three.js scene patterns, ES import maps, and interactive 3D setup. |
| `skills/threejs-scene-setup/SKILL.md` | Setting up Three.js WebGLRenderer, camera rigs, resize handling, and GPU disposal. |
| `skills/threejs-fundamentals/SKILL.md` | Core Three.js Object3D hierarchy, coordinate spaces, and render loop structure. |
| `skills/threejs-lighting/SKILL.md` | Designing light rigs (Ambient, Directional, Point, Spot, Hemisphere, RectArea), shadow maps, and IBL. |
| `skills/threejs-materials/SKILL.md` | Configuring PBR `MeshStandardMaterial`, `MeshPhysicalMaterial` (clearcoat, transmission), and surface properties. |
| `skills/threejs-materials-lighting/SKILL.md` | Debugging black/washed-out meshes, shadow acne, physically based intensities (r155+/r187), and tone mapping. |
| `skills/threejs-shaders/SKILL.md` | Writing custom Three.js `ShaderMaterial` GLSL vertex/fragment shaders and uniform pipelines. |
| `skills/shader-programming/SKILL.md` | Engine-neutral shader math (dissolve, outline, Fresnel rim, vignette, color grading) across GLSL and HLSL. |
| `skills/threejs-postprocessing/SKILL.md` | Configuring `EffectComposer`, bloom, DoF, SSAO, vignette, and color grading passes. |
| `skills/threejs-textures/SKILL.md` | UV mapping, normal/roughness/metalness/displacement maps, and texture encoding/optimization. |
| `skills/threejs-geometry/SKILL.md` | `BufferGeometry`, procedural meshes, and instanced rendering. |
| `skills/threejs-gltf-loading/SKILL.md` | Loading `.glb`/`.gltf` assets with Draco/KTX2 compression, normalizing scale, and binding env maps. |
| `skills/threejs-loaders/SKILL.md` | Async asset loading patterns for textures, HDR environment maps, and 3D models. |
| `skills/threejs-animation/SKILL.md` | Keyframe, skeletal (`SkinnedMesh`), and morph target animations in Three.js. |
| `skills/threejs-interaction/SKILL.md` | Raycasting, pointer picking, and `OrbitControls`/camera interaction. |
| `skills/spline-3d-integration/SKILL.md` | Embedding and controlling Spline.design 3D scenes in React or web apps. |
| `skills/lookdev/SKILL.md` | Standing up a local human-in-the-loop interactive control studio (sliders/presets) to tune lighting, color, and shader params by eye. |
| `skills/lookdev-auto/SKILL.md` | Running automated visual tuning loops where a vision/video model scores rendered variants. |
| `skills/algorithmic-art/SKILL.md` | Creating generative/computational art, mathematical patterns, and p5.js/Canvas visual systems. |

### 2. Art Direction, Visual Design & Aesthetic Systems (22)

| Skill | Read when |
|---|---|
| `skills/ckw-design/SKILL.md` | Establishing frontend art direction, visual philosophy, and design system entry point. |
| `skills/high-end-visual-design/SKILL.md` | Designing agency-grade interfaces with editorial typography, spatial rhythm, soft depth, and surface craft. |
| `skills/antigravity-design-expert/SKILL.md` | Building spatial, weightless, glassmorphic, and highly interactive UI architectures. |
| `skills/frontend-design/SKILL.md` | Avoiding generic AI-slop templates; shipping intentional, distinctive visual frontends. |
| `skills/design-taste-frontend/SKILL.md` | Enforcing calibrated color, typography, responsive grids, and anti-slop taste gates. |
| `skills/gpt-taste/SKILL.md` | Building GSAP-heavy editorial/marketing pages with wide hero typography and AIDA pacing. |
| `skills/minimalist-ui/SKILL.md` | Crafting clean editorial interfaces with warm monochrome palettes, crisp borders, and restrained motion. |
| `skills/industrial-brutalist-ui/SKILL.md` | Crafting raw industrial, tactical telemetry, rigid-grid, or CRT-inspired interfaces. |
| `skills/frontend-ui-dark-ts/SKILL.md` | Building dark-themed React + Tailwind + Framer Motion dashboards and control panels. |
| `skills/theme-factory/SKILL.md` | Applying curated font and color theme presets across web apps, slides, or artifacts. |
| `skills/brand-guidelines-community/SKILL.md` | Applying brand color palettes, typography pairings, and visual identity standards. |
| `skills/brand-perception-psychologist/SKILL.md` | Auditing subconscious visual/verbal brand perception signals via semiotics and repositioning. |
| `skills/visual-emotion-engineer/SKILL.md` | Mapping color, typography, spacing, and imagery style to targeted emotional responses. |
| `skills/premium-typography-kit/SKILL.md` | Pairing display and body fonts with optical hierarchy for mobile apps and landing pages. |
| `skills/iconsax-library/SKILL.md` | Selecting or generating consistent UI icon sets (Iconsax / vector icon systems). |
| `skills/favicon/SKILL.md` | Generating multi-size favicons, app icons, and manifest icon sets from a source asset. |
| `skills/canvas-design/SKILL.md` | Translating visual design philosophies into posters, compositions, and static visual artifacts. |
| `skills/json-canvas/SKILL.md` | Creating or editing `.canvas` visual node-and-edge boards. |
| `skills/design-orchestration/SKILL.md` | Routing multi-step design exploration through brainstorming, review, and build readiness. |
| `skills/product-design/SKILL.md` | Crafting end-to-end product visual systems, UX flows, and cohesive design languages. |
| `skills/product-inventor/SKILL.md` | Combining product thinking, design systems, cognitive psychology, and UI engineering for new concepts. |
| `skills/redesign-existing-projects/SKILL.md` | Auditing an existing app's generic UI patterns and upgrading its visual polish without breaking flows. |

### 3. UI/UX Architecture, Behavioral UX & Game UI/Feel (23)

| Skill | Read when |
|---|---|
| `skills/ui-ux-pro-max/SKILL.md` | Comprehensive UI/UX workflow for web/mobile apps: palettes, font pairings, layouts, and component craft. |
| `skills/ui-ux-designer/SKILL.md` | Creating wireframes, user flows, IA, and accessible interface specifications. |
| `skills/uxui-principles/SKILL.md` | Evaluating interfaces against research-backed UX/UI laws and detecting usability antipatterns. |
| `skills/ux-flow/SKILL.md` | Designing hub-and-spoke, progressive disclosure, and multi-step screen flows. |
| `skills/ux-audit/SKILL.md` | Auditing screens against Nielsen's heuristics and mobile/web UX ergonomics. |
| `skills/ux-copy/SKILL.md` | Writing clear microcopy for buttons, empty states, errors, toasts, and confirmations. |
| `skills/ux-feedback/SKILL.md` | Designing loading, skeleton, empty, error, and success feedback states. |
| `skills/ux-persuasion-engineer/SKILL.md` | Applying choice architecture and behavioral cues to reduce interaction friction ethically. |
| `skills/onboarding-psychologist/SKILL.md` | Designing first-use onboarding flows focused on early wins, clarity, and habit triggers. |
| `skills/emotional-arc-designer/SKILL.md` | Structuring emotional progression across landing pages, decks, or multi-step product flows. |
| `skills/loss-aversion-designer/SKILL.md` | Applying reference-point framing ethically to pricing, upgrade prompts, and UX copy. |
| `skills/information-hierarchy/SKILL.md` | Structuring visual hierarchy, progressive disclosure, and best-fit visual forms for dense outputs. |
| `skills/structured-artifact/SKILL.md` | Building self-contained static HTML artifacts with responsive layout, CSS vars, and dark-mode toggle. |
| `skills/game-ui-ux/SKILL.md` | Designing game HUDs, menus, safe areas, gamepad focus, and event-driven UI scaling. |
| `skills/game-feel/SKILL.md` | Tuning interactive visual juice: hitstop, camera shake, easing curves, particles, and feedback. |
| `skills/landing-page-generator/SKILL.md` | Building high-converting React/Tailwind landing pages structured around PAS/AIDA/BAB flows. |
| `skills/kpi-dashboard-design/SKILL.md` | Designing scannable KPI dashboards, metric cards, and executive data layouts. |
| `skills/interactive-portfolio/SKILL.md` | Crafting memorable interactive portfolios with strong case-study storytelling. |
| `skills/web-design-guidelines/SKILL.md` | Auditing web pages against modern Web Interface Guidelines (layout, contrast, focus, motion). |
| `skills/ui-skills/SKILL.md` | Applying strict opinionated UI constraints during interface generation. |
| `skills/ui-visual-validator/SKILL.md` | Running rigorous visual verification for layout alignment, overflow, contrast, and responsiveness. |
| `skills/deterministic-design/SKILL.md` | Running deterministic rendered layout audits (centroid, optical center, pixel balance). |
| `skills/unship/SKILL.md` | Comparing multiple agent-built UI variants locally in a live app, keeping the winner, and cleaning up temp code. |

### 4. Design Systems, Tokens, Components & Accessibility (24)

| Skill | Read when |
|---|---|
| `skills/design-md/SKILL.md` | Synthesizing semantic `DESIGN.md` specs from existing UI or Google Stitch projects. |
| `skills/stitch-design-taste/SKILL.md` | Authoring Google Stitch `DESIGN.md` systems with color, typography, layout, and motion intent. |
| `skills/stitch-ui-design/SKILL.md` | Crafting structured UI generation prompts for Google Stitch. |
| `skills/stitch-loop/SKILL.md` | Running iterative multi-page Stitch UI build loops. |
| `skills/figma-automation/SKILL.md` | Reading/updating Figma files, components, design tokens, comments, and asset exports via MCP. |
| `skills/canva-automation/SKILL.md` | Managing Canva designs, brand templates, autofill, and exports via MCP. |
| `skills/rayden-use/SKILL.md` | Building and maintaining Rayden UI components and screens in Figma with token enforcement. |
| `skills/rayden-code/SKILL.md` | Generating React code using Rayden UI components, props, and tokens. |
| `skills/shadcn/SKILL.md` | Scaffolding, customizing, and theming `shadcn/ui` components and registries. |
| `skills/radix-ui-design-system/SKILL.md` | Building accessible headless component systems with Radix UI primitives. |
| `skills/core-components/SKILL.md` | Structuring core design system component primitives and token contracts. |
| `skills/baseline-ui/SKILL.md` | Enforcing typography scale, animation duration bounds, accessibility, and layout safety. |
| `skills/tailwind-design-system/SKILL.md` | Building token-driven design systems and component variants with Tailwind CSS. |
| `skills/tailwind-patterns/SKILL.md` | Applying Tailwind CSS v4 CSS-first `@theme`, container queries, and modern token patterns. |
| `skills/react-ui-patterns/SKILL.md` | Implementing clean loading, error, and data-display UI patterns in React. |
| `skills/angular-ui-patterns/SKILL.md` | Implementing clean loading, error, and data-display UI patterns in Angular. |
| `skills/ui-setup/SKILL.md` | Bootstrapping StyleSeed app color, visual style, typography, and initial token setup. |
| `skills/ui-tokens/SKILL.md` | Listing, adding, and syncing StyleSeed design tokens across JSON, CSS variables, and dark mode. |
| `skills/ui-component/SKILL.md` | Generating UI components following StyleSeed structure, tokens, and accessibility rules. |
| `skills/ui-pattern/SKILL.md` | Composing reusable card sections, grids, lists, forms, and chart wrappers. |
| `skills/ui-page/SKILL.md` | Scaffolding mobile-first pages with consistent section rhythm and shell structure. |
| `skills/ui-review/SKILL.md` | Reviewing UI code for token compliance, spacing discipline, and mobile ergonomics. |
| `skills/ui-a11y/SKILL.md` | Auditing and fixing WCAG 2.2 AA contrast, keyboard navigation, semantics, and focus management. |
| `skills/screen-reader-testing/SKILL.md` | Validating ARIA landmarks, live regions, and screen reader flows in web apps. |

### 5. Mobile & Apple HIG UI (19)

| Skill | Read when |
|---|---|
| `skills/mobile-design/SKILL.md` | Designing touch-first, mobile-first layouts, hit targets, and platform-respectful navigation. |
| `skills/building-native-ui/SKILL.md` | Building polished native UIs with Expo Router, navigation, and native styling primitives. |
| `skills/expo-tailwind-setup/SKILL.md` | Setting up Tailwind CSS v4 with `react-native-css` and NativeWind v5 in Expo. |
| `skills/expo-ui-jetpack-compose/SKILL.md` | Integrating Jetpack Compose native UI views inside Expo apps. |
| `skills/android-jetpack-compose-expert/SKILL.md` | Building Material Design 3 Android UIs in Jetpack Compose with clean state & performance. |
| `skills/hig-project-context/SKILL.md` | Creating or updating `.claude/apple-design-context.md` shared across Apple HIG skills. |
| `skills/hig-foundations/SKILL.md` | Applying Apple HIG color, typography, layout, dark mode, and spatial foundations. |
| `skills/hig-platforms/SKILL.md` | Adapting UI across iOS, iPadOS, macOS, visionOS, and watchOS conventions. |
| `skills/hig-patterns/SKILL.md` | Applying Apple HIG interaction, onboarding, feedback, and navigation patterns. |
| `skills/hig-inputs/SKILL.md` | Designing touch, pointer, keyboard, Apple Pencil, and focus-based inputs per Apple HIG. |
| `skills/hig-technologies/SKILL.md` | Integrating Apple system UI technologies (SF Symbols, Live Activities, SharePlay, etc.). |
| `skills/hig-components-content/SKILL.md` | Designing Apple HIG content display views (lists, collections, cards, charts). |
| `skills/hig-components-controls/SKILL.md` | Designing Apple HIG controls (buttons, toggles, pickers, sliders, segmented controls). |
| `skills/hig-components-dialogs/SKILL.md` | Designing Apple HIG sheets, popovers, alerts, and confirmation dialogs. |
| `skills/hig-components-layout/SKILL.md` | Designing Apple HIG navigation bars, tab bars, sidebars, and split views. |
| `skills/hig-components-menus/SKILL.md` | Designing Apple HIG context menus, pull-down menus, and toolbars. |
| `skills/hig-components-search/SKILL.md` | Designing Apple HIG search fields, scopes, and token-based filtering. |
| `skills/hig-components-status/SKILL.md` | Designing Apple HIG progress indicators, gauges, and activity states. |
| `skills/hig-components-system/SKILL.md` | Designing Apple HIG widgets, notifications, and lock-screen/system surfaces. |

### 6. Motion, Animation & Data Visualization (9)

| Skill | Read when |
|---|---|
| `skills/animejs-animation/SKILL.md` | Building choreographed timeline, SVG, or DOM animations with Anime.js. |
| `skills/magic-animator/SKILL.md` | Designing motion concepts for logos, UI icons, micro-animations, and social assets. |
| `skills/magic-ui-generator/SKILL.md` | Generating and comparing animated UI component variants (21st.dev / Magic UI patterns). |
| `skills/design-spells/SKILL.md` | Adding subtle micro-interactions, tactile hover/press states, and personality details. |
| `skills/scroll-experience/SKILL.md` | Building scroll-linked storytelling, parallax depth, and viewport-triggered choreography. |
| `skills/vercel-react-view-transitions/SKILL.md` | Implementing React/Next.js View Transitions API route and shared-element animations. |
| `skills/fixing-motion-performance/SKILL.md` | Auditing and eliminating layout thrashing, non-compositor animations, and scroll jank. |
| `skills/claude-d3js-skill/SKILL.md` | Building bespoke interactive SVG/Canvas data visualizations, graphs, and charts with D3.js. |
| `skills/mermaid-expert/SKILL.md` | Creating styled Mermaid flowcharts, sequence diagrams, ERDs, and architecture visuals. |

### 7. AI Visual, Image, Presentation & Video Media Production (25)

| Skill | Read when |
|---|---|
| `skills/image-studio/SKILL.md` | Routing image generation across Gemini/AI Studio (photorealistic) and Stability AI (art/assets). |
| `skills/ai-studio-image/SKILL.md` | Generating realistic, humanized photography and editorial portraits via Google AI Studio. |
| `skills/imagen/SKILL.md` | Generating UI placeholders, illustrations, and visual assets with Google Gemini/Imagen. |
| `skills/stability-ai/SKILL.md` | Generating, editing, inpainting, upscaling, and removing backgrounds with Stability AI (SD3.5/Ultra). |
| `skills/comfyui-gateway/SKILL.md` | Orchestrating ComfyUI REST workflows, node graphs, queuing, and batch image generation. |
| `skills/fal-generate/SKILL.md` | Generating AI images and videos via `fal.ai` models. |
| `skills/fal-image-edit/SKILL.md` | Performing AI style transfer, inpainting, and object removal via `fal.ai`. |
| `skills/fal-upscale/SKILL.md` | Upscaling and enhancing image or video resolution via `fal.ai`. |
| `skills/fal-workflow/SKILL.md` | Chaining multi-step `fal.ai` generation/edit/upscale pipelines via workflow JSON. |
| `skills/fal-platform/SKILL.md` | Inspecting `fal.ai` model catalogs, pricing, and usage metrics. |
| `skills/fal-audio/SKILL.md` | Generating TTS/audio tracks paired with visual/video media via `fal.ai`. |
| `skills/mmx-cli/SKILL.md` | Generating images, videos, speech, and music via the MiniMax `mmx` CLI. |
| `skills/runapi-cli/SKILL.md` | Generating AI images, videos, and audio from the terminal via RunAPI CLI. |
| `skills/vizcom/SKILL.md` | Transforming industrial/product sketches into full-fidelity 3D renders with Vizcom. |
| `skills/create-game-assets/SKILL.md` | Planning, generating, and QA-checking consistent sprites, tilesets, icons, and textures with style guides. |
| `skills/article-illustrations/SKILL.md` | Creating hand-drawn 16:9 editorial article illustrations with consistent visual style. |
| `skills/photopea-embedded-editor/SKILL.md` | Embedding and scripting Photopea (`photopea.js`) for in-app PSD/layer image editing. |
| `skills/unsplash-integration/SKILL.md` | Searching and integrating licensed high-resolution photography from Unsplash. |
| `skills/nanobanana-ppt-skills/SKILL.md` | Generating styled presentation decks with document analysis and custom visual slides. |
| `skills/screenshots/SKILL.md` | Capturing HiDPI (2x Retina) marketing and documentation screenshots with Playwright. |
| `skills/screenstudio-alt/SKILL.md` | Post-producing UI screen recordings headlessly (auto-zoom on clicks, cursor smoothing, keystroke overlays, 9:16 export). |
| `skills/slack-gif-creator/SKILL.md` | Building optimized animated GIFs for product demos, UI previews, and Slack. |
| `skills/remotion/SKILL.md` | Generating automated product walkthrough videos from Stitch/web projects using Remotion. |
| `skills/remotion-best-practices/SKILL.md` | Writing clean, deterministic React-based video compositions in Remotion. |
| `skills/videodb/SKILL.md` | Indexing, editing timelines, adding overlays/subtitles, and generating AI video media via VideoDB. |

---

## How to work

**Do not generate boilerplate UI or uncalibrated 3D scenes blindly on the first reply.**

1. **Inspect the workspace first.** Check `package.json`, `tailwind.config.*`, CSS variables / `DESIGN.md`, `tsconfig.json`, existing component libraries (`shadcn`, Radix, MUI, Compose), and Three.js/WebGL versions before proposing styles or code.
2. **Clarify missing visual constraints.** If target platform (web, mobile, 3D/WebGL, game HUD), aesthetic direction, or existing brand tokens are unclear, ask concise targeted questions before building. Skip questions the codebase or prompt already answers.
3. **Execute in visual layers.**
   - **Direction & Hierarchy:** Lock aesthetic tokens (`DESIGN.md`, color palette, typography, UX flow) before writing components.
   - **3D & Lighting:** Verify geometry (`MeshNormalMaterial` check) -> material choice (`MeshStandardMaterial` / `MeshPhysicalMaterial`) -> IBL + key/fill/rim light rig + tone mapping -> shaders/post-processing.
   - **Implementation & Motion:** Compose accessible components (`ui-a11y`, `baseline-ui`) and compositor-safe motion (`fixing-motion-performance`).
4. **Verify visually before claiming done.** Audit layout balance, contrast (WCAG 2.2 AA), responsiveness, and motion performance (`ui-visual-validator`, `deterministic-design`, `lookdev` / `screenshots`). When generating multiple UI variants (`unship`), clean up unused temporary code after selection.

## Boundaries

- **No generic AI-slop defaults:** Avoid unrequested purple/blue SaaS gradients, rainbow glows, cramped cards, or default system fonts when intentional art direction is expected.
- **Respect existing design systems:** Never overwrite existing `DESIGN.md`, Tailwind `@theme` tokens, or component primitives unless explicitly asked to redesign.
- **Three.js lighting calibration:** Do not use legacy pre-r155 light intensity values (`intensity: 1` without IBL/tone mapping) on modern Three.js scenes; always check the installed `three` version in `package.json`.
- **Compositor-only motion:** Never animate layout-triggering properties (`width`, `height`, `top`, `left`, `margin`) when `transform` and `opacity` can achieve the effect.
- **Clean up visual experiments:** Remove temporary lookdev harnesses, unused UI variants, or scratch screenshot scripts once verified unless the user asks to keep them.
