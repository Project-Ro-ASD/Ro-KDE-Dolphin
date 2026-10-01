# Architecture

## Purpose

Ro-KDE-Dolphin is the Ro-ASD downstream customization layer for the KDE Dolphin file manager.
It is not a replacement file manager, it is not a full fork and it does not own general desktop theming.

## Ownership boundaries

This repository may own:

- Dolphin-specific source patches in the user interface layer
- Dolphin menu, toolbar and context menu changes
- Dolphin label, tooltip and translation changes
- Dolphin-specific icons or illustrations when they are not general theme assets
- Fedora packaging required to ship those downstream changes

This repository must not become the source of truth for:

- KIO, file operations, permissions, trash, mounting or any other file system backend
- global Plasma themes, icon themes, Kvantum styles, window decorations, wallpapers or cursors: Ro-Theme
- distribution identity and generic branding contracts: ro-asd-branding
- generic desktop/system defaults: ro-asd-defaults
- System Settings: Ro-KDE-SystemSettings
- unrelated KDE application patches

## Frontend / backend line inside Dolphin

Dolphin is a QtWidgets (C++) application. There is no QML layer to override.

Considered UI layer (patchable when an override is not enough):

- `src/dolphinmainwindow.*`, `src/dolphintabbar.*`, `src/dolphintabwidget.*`
- `src/views/`, `src/kitemviews/` (rendering and layout only)
- `src/panels/`, `src/statusbar/`, `src/filterbar/`, `src/selectionmode/`
- `src/dolphinui.rc` (prefer kxmlgui override instead of patching)
- `src/settings/` (dialog presentation only, not setting semantics)

Considered backend and out of scope:

- anything delegating to KIO jobs (copy, move, delete, trash, permissions)
- `src/admin/` (privileged/administrator mode)
- search engine integration logic in `src/search/`
- model data loading in `src/kitemviews/kfileitemmodel*` beyond presentation

## Downstream model

Prefer the smallest possible downstream delta.

1. Use configuration (kcfg defaults) or kxmlgui overrides when possible.
2. Use service menu, translation or asset overrides when the upstream contract allows them.
3. Use patches only when an override cannot express the required change.
4. Keep each patch scoped to one upstream project and one reason.
5. Never vendor a complete KDE source tree into this repository.

## Repository layers

- `patches/`: source patches grouped by upstream KDE project
- `overrides/`: kxmlgui, service menu and translation overrides
- `assets/`: Dolphin-specific visual assets
- `packaging/`: Fedora/RPM integration
- `scripts/`: validation and maintenance helpers
- `tests/`: smoke and contract tests
- `docs/`: architecture, upstream mapping and provenance template

## Compatibility

Every downstream change should record the upstream project and compatible version or tag range before it is considered release-ready. Dolphin follows the KDE Gear release cycle (YY.MM tags), not the Plasma cycle.
