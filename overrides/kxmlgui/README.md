# kxmlgui override: dolphinui.rc

- Upstream file: https://invent.kde.org/system/dolphin.git `src/dolphinui.rc`
- Upstream base tag: v26.08.1 (Fedora 44 package: dolphin-26.08.1-1.fc44)
- Upstream ui.rc version: 49 (kept unchanged on purpose)
- Changed section: `mainToolBar` only. Menus and ActionProperties are identical to upstream.

## Why the whole file is copied

KXMLGUI loads one complete ui.rc document; it cannot merge a partial file. Keep the diff against upstream limited to `mainToolBar`.

## Change (Ro-ASD design)

Upstream toolbar: go_back, go_forward, view_settings, url_navigators, split_view, split_stash, toggle_search, hamburger_menu

Ro-ASD toolbar: go_back, go_forward, url_navigators, toggle_search, icons, details, compact, split_view, hamburger_menu

## Version rule

The `version` attribute stays equal to upstream (49). When a newer Dolphin ships a higher version, KXMLGUI prefers the upstream file and Dolphin falls back to the stock toolbar instead of breaking. On every Dolphin update: diff upstream `src/dolphinui.rc` against this file, re-apply the toolbar change and set the new version.

## Local test

    mkdir -p ~/.local/share/kxmlgui5/dolphin
    cp overrides/kxmlgui/dolphinui.rc ~/.local/share/kxmlgui5/dolphin/dolphinui.rc
