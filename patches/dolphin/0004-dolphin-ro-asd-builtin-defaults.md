## 0004-dolphin-ro-asd-builtin-defaults

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0003
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/settings/dolphin_generalsettings.kcfg (ShowStatusBar)
  - src/settings/dolphin_contentdisplaysettings.kcfg (DirectorySizeMode, UseShortRelativeDates)
  - src/settings/dolphin_directoryviewpropertysettings.kcfg (ViewMode, PreviewsShown, VisibleRoles)
- Layer: settings defaults only. No code paths change.
- Reason (Ro-ASD): built-in defaults for the Ro-ASD design, decided in docs/DEFAULTS.md. Avoids /etc/skel and first-login scripts; user settings always override.
- Override considered: /etc/xdg/dolphinrc cannot provide view properties (stored per user as xattr), so all Dolphin defaults live in kcfg for one consistent mechanism.
- Upstreamable: no, distribution-specific.
- Verification: built against v26.08.1 + 0001-0003, ran build/bin/dolphin with empty XDG_CONFIG_HOME and XDG_DATA_HOME; opens in details view without previews, columns Name/Modified/Size/Type, absolute dates, "—" for folder size, full-width status bar.
- Upgrade risk: low. On each Dolphin release check that the six kcfg entries still exist with the same names.
