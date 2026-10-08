# Dolphin defaults

## Ownership (team decision)

- Dolphin-specific defaults (view mode, sorting, previews, columns, status bar, Dolphin toolbar/menu behavior): Ro-KDE-Dolphin
- Shared or generic KDE/Plasma defaults used by several applications: ro-asd-defaults
- ro-asd-defaults currently installs no /etc/xdg/dolphinrc or other Dolphin config, so there is no RPM file ownership conflict.

## Mechanism

1. Preferred: change Dolphin's own KCFG defaults with a downstream patch (patch 0004).
2. Not used: /etc/skel (forbidden by the defaults policy, xattrs are not reliable there).
3. Not used: first-login scripts (adds state and migration problems in $HOME).
4. Possible later stage: a vendor default fallback in ViewProperties::defaultProperties() (for example /usr/share/ro-asd/dolphin/...) if defaults must change without rebuilding Dolphin. Not needed now.

Resulting behavior: Ro-ASD built-in default, then the user's own dolphinrc / xattr view properties always win.

## Current Ro-ASD defaults (patch 0004)

| Setting | File | Upstream | Ro-ASD | Design reason |
| --- | --- | --- | --- | --- |
| ShowStatusBar | dolphin_generalsettings.kcfg | Small | FullWidth | full-width status bar |
| DirectorySizeMode | dolphin_contentdisplaysettings.kcfg | ContentCount | None | "—" for folders (patch 0001) |
| UseShortRelativeDates | dolphin_contentdisplaysettings.kcfg | true | false | absolute dates |
| ViewMode | dolphin_directoryviewpropertysettings.kcfg | Icons | Details | details view |
| PreviewsShown | dolphin_directoryviewpropertysettings.kcfg | true | false | small monochrome icons |
| VisibleRoles | dolphin_directoryviewpropertysettings.kcfg | empty (size, date) | Modified, Size, Type | design column order |
| IconSize (IconsMode) | dolphin_iconsmodesettings.kcfg | 32 | 48 | icon view cards (patch 0008) |
| ShowSelectionToggle | dolphin_generalsettings.kcfg | true | false | no hover "+" marker (patch 0010) |

Already matching upstream, not patched: HighlightEntireRow=true, ExpandableFolders=true, ShowZoomSlider=false, SortRole=text, SortFoldersFirst=true.

## Testing defaults as a new user

    T=/tmp/ro-dolphin-test; rm -rf $T; mkdir -p $T/config $T/data
    XDG_CONFIG_HOME=$T/config XDG_DATA_HOME=$T/data .work/upstream/dolphin/build/bin/dolphin

Theme colors look wrong in this empty profile because kdeglobals is missing; only Dolphin defaults are being tested.
