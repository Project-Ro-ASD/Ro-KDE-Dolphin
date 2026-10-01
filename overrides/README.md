# Overrides

Prefer overrides over source patches when KDE provides a stable override path. Dolphin has no QML layer, so the useful override paths are:

- `kxmlgui/`: Dolphin menu and toolbar layout (`dolphinui.rc`). KXMLGUI picks the file with the higher `version` attribute, so a downstream copy must track the upstream version and be re-checked on every Dolphin update.
- `servicemenus/`: Dolphin context menu actions as `.desktop` service menu files.
- `translations/`: Ro-ASD specific downstream strings and `.po` files (`dolphin.po`). Prefer contributing translation fixes to KDE upstream first.

Do not put here:

- Kvantum, Klassy, color schemes or icon themes: Ro-Theme
- system wide `dolphinrc` / `/etc/xdg` defaults and the shared Places list: ro-asd-defaults (agree with that repository before adding any Dolphin default here)

Do not copy whole upstream files when only one entry changes; keep the delta minimal and documented.
