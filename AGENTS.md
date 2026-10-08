# AGENTS.md

This repository is the Ro-ASD downstream customization layer for KDE Dolphin.

## Read first

Before making any implementation change, read README.md, docs/ARCHITECTURE.md, docs/UPSTREAM-COMPONENTS.md, docs/DEVELOPMENT.md, docs/PATCH-PROVENANCE-TEMPLATE.md, .roasd/component.json and .roasd/upstreams.json.

## Scope

This repository may own only Dolphin-specific downstream user interface changes.

Allowed examples:
- Dolphin menu and toolbar layout (kxmlgui)
- Dolphin context menu entries (service menus)
- Dolphin labels, tooltips and Turkish/Ro-ASD strings
- Dolphin-specific icons or illustrations
- narrowly scoped widget/UI source patches (views, panels, status bar, main window)
- Fedora packaging for those changes

Do not move these responsibilities into this repository:
- KIO, KIO workers, file operations, permissions, trash or mounting logic: upstream KDE, not patched here
- global Plasma themes, icon themes, Kvantum styles, window decorations, wallpapers or cursors: Ro-Theme
- generic distribution branding: ro-asd-branding
- generic desktop/system defaults, including the shared Places list used by all file dialogs: ro-asd-defaults
- System Settings changes: Ro-KDE-SystemSettings
- unrelated KDE application modifications

## Working rules

- Never vendor a full KDE source tree into this repository.
- Use scripts/fetch-upstream.sh to create disposable upstream checkouts under .work/upstream/.
- Prefer configuration, kxmlgui or service menu override over source patch.
- Prefer a narrow source patch over a fork.
- Source patches must stay in the UI layer. Do not change file operation, KIO job or privilege logic for visual customization.
- Confirm the real KDE upstream owner before editing or creating a patch.
- One patch should have one reason.
- Every patch needs a provenance note based on docs/PATCH-PROVENANCE-TEMPLATE.md.
- Do not commit build directories, cloned upstream trees, RPM outputs, .orig or .rej files.
- Do not add install scripts that write into /usr or overwrite files owned by other packages.
- Production packaging is a Fedora package-name-preserving rebuild (see packaging/fedora/README.md). Release only through .github/workflows/release.yml; never commit signing keys, RPMs or release assets.

## Git workflow

Do not work directly on main. Use a descriptive feature/, patch/ or docs/ branch, open a pull request and keep commits reviewable and scoped. Use conventional commit prefixes (feat, fix, docs, chore, ci, dev).

## Before editing upstream code

1. Run: bash scripts/check-env.sh
2. Fetch only the needed upstream project: bash scripts/fetch-upstream.sh dolphin
3. Check out the tag matching the Dolphin version shipped in Fedora 44.
4. Identify the exact upstream file and behavior.
5. Decide whether the requested change belongs in an override or a patch.
6. Record the upstream base revision in the patch provenance note.

## Validation

At minimum run:

    python3 scripts/validate.py

When a real patch or override exists, add a focused smoke test for it under tests/.

## Handoff expectation

When finishing a task, report:
- what changed
- which KDE upstream project owns the affected code
- whether the solution is override or patch
- upstream base revision used
- tests run and their results
- any compatibility or upgrade risk
- files changed in this repository

If the requested change crosses an ownership boundary, stop that part of the implementation and explain which Ro-ASD repository should own it.
