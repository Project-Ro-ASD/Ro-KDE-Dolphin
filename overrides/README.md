# Overrides

Prefer overrides over source patches when KDE provides a stable override path. Dolphin has no QML layer, so the useful override paths are:

- `kxmlgui/`: Dolphin menu and toolbar layout (`dolphinui.rc`). KXMLGUI picks the file with the higher `version` attribute, so a downstream copy must track the upstream version and be re-checked on every Dolphin update.
- `servicemenus/`: Dolphin context menu actions as `.desktop` service menu files.
- `translations/`: Ro-ASD translation domain `ro-kde-dolphin` (`ro-kde-dolphin.po`). Strings added by Ro-ASD patches use `i18nd("ro-kde-dolphin", ...)` so Dolphin's own catalog is never replaced. Packaging installs the compiled .mo to `/usr/share/locale/<lang>/LC_MESSAGES/ro-kde-dolphin.mo`. Fixes to existing Dolphin strings go to KDE upstream.

Do not put here:

- Kvantum, Klassy, color schemes or icon themes: Ro-Theme
- shared/generic KDE and Plasma defaults and the shared Places list: ro-asd-defaults. Dolphin-specific defaults belong to Ro-KDE-Dolphin and are built in as KCFG defaults (see docs/DEFAULTS.md), not shipped as /etc/xdg files.

Do not copy whole upstream files when only one entry changes; keep the delta minimal and documented.
