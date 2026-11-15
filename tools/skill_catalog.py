"""Search, inspect, and validate the 142 skills in ui-ux-visual-lighting-skills without flooding context."""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
AGENTS_MD = os.path.join(ROOT, "AGENTS.md")


def _extract_meta(skill_name):
    sf = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    if not os.path.isfile(sf):
        return {"name": skill_name, "desc": "", "body": ""}
    raw = open(sf, encoding="utf-8", errors="ignore").read()
    desc = ""
    m = re.search(r'(?ms)^description:\s*(?:>-\s*\r?\n\s*|\|\s*\r?\n\s*)?(.+?)(?:\r?\n[a-zA-Z_-]+:|\r?\n---)', raw)
    if m:
        desc = re.sub(r"\s+", " ", m.group(1)).strip().strip('"\'')
    return {"name": skill_name, "desc": desc, "body": raw}


def _all_skills():
    return sorted(
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d))
    )


def cmd_list(args):
    skills = _all_skills()
    print(f"Total skills: {len(skills)}")
    for s in skills:
        meta = _extract_meta(s)
        d = meta["desc"]
        if len(d) > 100:
            d = d[:97] + "..."
        print(f"  {s:<34} {d}")


def cmd_find(args):
    terms = [t.lower() for t in args.query]
    scored = []
    for s in _all_skills():
        meta = _extract_meta(s)
        hay_name = s.lower()
        hay_desc = meta["desc"].lower()
        hay_body = meta["body"][:2500].lower()
        score = 0
        for t in terms:
            if t in hay_name:
                score += 6
            if t in hay_desc:
                score += 4
            if t in hay_body:
                score += 1
        if score > 0:
            scored.append((score, s, meta["desc"]))
    scored.sort(key=lambda x: (-x[0], x[1]))
    if not scored:
        print(f"No matches for: {' '.join(args.query)}")
        return
    for score, s, desc in scored[: args.limit]:
        if len(desc) > 110:
            desc = desc[:107] + "..."
        print(f"[{score:2}] skills/{s}/SKILL.md — {desc}")


def cmd_inspect(args):
    sf = os.path.join(SKILLS_DIR, args.skill, "SKILL.md")
    if not os.path.isfile(sf):
        sys.exit(f"[ERR] Skill not found: {args.skill}")
    lines = open(sf, encoding="utf-8", errors="ignore").read().splitlines()
    for line in lines[: args.lines]:
        print(line)
    if len(lines) > args.lines:
        print(f"\n... ({len(lines) - args.lines} more lines in skills/{args.skill}/SKILL.md)")


def cmd_verify(args):
    disk = _all_skills()
    agents_txt = open(AGENTS_MD, encoding="utf-8").read()
    listed = sorted(set(re.findall(r"skills/([a-zA-Z0-9._-]+)/SKILL\.md", agents_txt)))
    missing = [s for s in disk if s not in listed]
    phantom = [s for s in listed if s not in disk]

    # Check symlinks/junctions
    links = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for name in dirnames + filenames:
            p = os.path.join(dirpath, name)
            if os.path.islink(p):
                links.append(p)

    # Check manifests
    json_errs = []
    for rel in ("plugin.json", "gemini-extension.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        try:
            json.load(open(os.path.join(ROOT, rel), encoding="utf-8"))
        except Exception as exc:
            json_errs.append(f"{rel}: {exc}")

    # Check SKILL.md presence & descriptions
    bad_skills = []
    for s in disk:
        meta = _extract_meta(s)
        if not meta["body"] or not meta["desc"] or "One sentence - what this skill does" in meta["desc"]:
            bad_skills.append(s)

    print(f"Disk skills      : {len(disk)}")
    print(f"AGENTS.md skills : {len(listed)}")
    print(f"Missing/Phantom  : {len(missing)} / {len(phantom)}")
    print(f"Symlinks         : {len(links)}")
    print(f"JSON errors      : {len(json_errs)}")
    print(f"Bad SKILL.md     : {len(bad_skills)}")

    if missing or phantom or links or json_errs or bad_skills:
        for item in missing:
            print(f"  [MISSING IN AGENTS.MD] {item}")
        for item in phantom:
            print(f"  [PHANTOM IN AGENTS.MD] {item}")
        for item in json_errs:
            print(f"  [JSON ERR] {item}")
        for item in bad_skills:
            print(f"  [BAD SKILL] {item}")
        sys.exit(1)
    print("[OK] Skillset integrity verified.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Search, inspect, and verify ui-ux-visual-lighting-skills.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List all 142 skills with 1-line descriptions")
    p_list.set_defaults(func=cmd_list)

    p_find = sub.add_parser("find", help="Search skills by keyword")
    p_find.add_argument("query", nargs="+", help="Search keywords")
    p_find.add_argument("--limit", type=int, default=12, help="Max results")
    p_find.set_defaults(func=cmd_find)

    p_ins = sub.add_parser("inspect", help="Print the top lines of a skill's SKILL.md")
    p_ins.add_argument("skill", help="Skill folder name")
    p_ins.add_argument("--lines", type=int, default=60, help="Lines to print")
    p_ins.set_defaults(func=cmd_inspect)

    p_ver = sub.add_parser("verify", help="Verify pack parity, manifests, SKILL.md frontmatter, and zero links")
    p_ver.set_defaults(func=cmd_verify)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
