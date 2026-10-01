#!/usr/bin/env python3
"""Ro-KDE-Dolphin repository contract validator."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = "ro-kde-dolphin"
errors = []

required = [
    "README.md",
    "VERSION",
    "AGENTS.md",
    "LICENSE",
    ".roasd/component.json",
    ".roasd/upstreams.json",
    "docs/ARCHITECTURE.md",
    "docs/UPSTREAM-COMPONENTS.md",
    "docs/DEVELOPMENT.md",
    "docs/PATCH-PROVENANCE-TEMPLATE.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

# Component metadata
try:
    meta = json.loads((ROOT / ".roasd" / "component.json").read_text())
    if meta.get("component_type") != "component":
        errors.append("component_type must be 'component'")
    if meta.get("component") != COMPONENT:
        errors.append(f"component must be '{COMPONENT}'")
except Exception as exc:
    errors.append(f"invalid component metadata: {exc}")

# Upstream map
known_projects = set()
try:
    upstreams = json.loads((ROOT / ".roasd" / "upstreams.json").read_text())
    known_projects = set(upstreams.get("projects", {}))
    if not known_projects:
        errors.append("upstreams.json must list at least one project")
except Exception as exc:
    errors.append(f"invalid upstream metadata: {exc}")

# Version
version_file = ROOT / "VERSION"
version = version_file.read_text().strip() if version_file.exists() else ""
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    errors.append("VERSION must contain a semantic version such as 0.1.0")

# Patches: known upstream folder, ordered name, provenance note
patches_dir = ROOT / "patches"
for patch in sorted(patches_dir.rglob("*.patch")):
    rel = patch.relative_to(ROOT)
    project = patch.parent.name
    if patch.parent.parent != patches_dir or project not in known_projects:
        errors.append(f"{rel}: patch must live in patches/<known upstream project>/")
    if not re.fullmatch(r"\d{4}-[a-z0-9][a-z0-9-]*\.patch", patch.name):
        errors.append(f"{rel}: name must look like 0001-dolphin-short-description.patch")
    if not patch.with_suffix(".md").exists():
        errors.append(f"{rel}: missing provenance note {patch.with_suffix('.md').name}")

# No vendored upstream trees or build leftovers
for marker in ("CMakeLists.txt", "dolphinmainwindow.cpp"):
    for hit in ROOT.rglob(marker):
        if ".work" in hit.parts or ".git" in hit.parts:
            continue
        errors.append(f"{hit.relative_to(ROOT)}: looks like vendored upstream source")
for pattern in ("*.orig", "*.rej", "*.rpm"):
    for hit in ROOT.rglob(pattern):
        if ".work" in hit.parts or ".git" in hit.parts:
            continue
        errors.append(f"{hit.relative_to(ROOT)}: build or patch leftover must not be committed")

# Ownership boundary: global theming belongs to Ro-Theme
for forbidden in ("theme", "kvantum", "klassy", "icons", "wallpapers", "cursors"):
    path = ROOT / "overrides" / forbidden
    if path.exists():
        errors.append(f"overrides/{forbidden}: global theming belongs to Ro-Theme")

if errors:
    print("validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Ro-KDE-Dolphin repository contract: OK")
