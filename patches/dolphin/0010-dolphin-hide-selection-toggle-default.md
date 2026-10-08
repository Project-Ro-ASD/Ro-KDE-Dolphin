## 0010-dolphin-hide-selection-toggle-default

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0009
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/settings/dolphin_generalsettings.kcfg (ShowSelectionToggle default false, upstream true)
- Layer: settings default only.
- Reason (Ro-ASD): the design has no "+" selection marker on hover. Users can turn it back on in Dolphin settings; their setting always wins (docs/DEFAULTS.md).
- Override considered: no system config file is used for Dolphin defaults (team decision, docs/DEFAULTS.md).
- Upstreamable: no, distribution-specific.
- Verification: built against v26.08.1 + 0001-0009 with the user key removed; no marker on hover, click / Ctrl+click selection unchanged.
- Upgrade risk: low. Check that the entry still exists on the next Dolphin release.
