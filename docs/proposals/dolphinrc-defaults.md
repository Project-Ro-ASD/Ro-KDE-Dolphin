# Proposal: Dolphin settings defaults for the Ro-ASD design

Status: proposal. Not installed by this repository. System-wide defaults may belong to `ro-asd-defaults`; agree on the owner before shipping.

Upstream reference: dolphin v26.08.1 (`src/settings/*.kcfg`, `src/views/viewproperties.cpp`). All values below were tested locally against the design mockups.

## 1. dolphinrc

    [General]
    ShowStatusBar=FullWidth
    ShowZoomSlider=false

    [DetailsMode]
    HighlightEntireRow=true
    ExpandableFolders=true

    [ContentDisplay]
    UseShortRelativeDates=false

- ShowStatusBar=FullWidth: full-width status bar instead of the floating bubble
- ShowZoomSlider=false: design has no zoom slider
- HighlightEntireRow=true: selection fills the whole row
- ExpandableFolders=true: folders open in place with a chevron
- UseShortRelativeDates=false: absolute dates (1.10.2026 16:34) instead of "26 minutes ago"

## 2. Global view properties

With `GlobalViewProps=true` (Dolphin default) these are stored as the extended attribute `user.kde.fm.viewproperties#1` on `~/.local/share/dolphin/view_properties/global`, not in a config file.

    [Dolphin]
    Version=4
    ViewMode=1
    PreviewsShown=false
    VisibleRoles=CustomizedDetails,Details_text,Details_modificationtime,Details_size,Details_type

- ViewMode=1: details view by default
- PreviewsShown=false: small monochrome icons instead of thumbnails
- VisibleRoles: columns Name, Modified, Size, Type in the design order

Read on a test machine:

    getfattr -n "user.kde.fm.viewproperties#1" --only-values ~/.local/share/dolphin/view_properties/global

## Open questions

- Owner of system-wide defaults: this repository or `ro-asd-defaults`?
- Shipping mechanism for view properties: they live in per-user xattrs, so `/etc/xdg` cannot provide them. Options: first-login script, `/etc/skel` seeding, or a small Dolphin patch that reads a system default.
- Not solvable by settings, handled by later patches: folder size shown as "—", status bar disk space indicator, row height and header style.
- Type column shows "Folder" untranslated for directories: comes from shared-mime-info, not Dolphin.
