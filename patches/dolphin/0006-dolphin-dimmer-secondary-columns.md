## 0006-dolphin-dimmer-secondary-columns

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0005
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/kitemviews/kstandarditemlistwidget.cpp (updateAdditionalInfoTextColor)
- Layer: UI color only.
- Reason (Ro-ASD): secondary columns (Modified, Size, Type) use the color scheme's inactive text color, KColorScheme(Active, View).foreground(InactiveText), so Ro-Theme decides how dim they are. Requested by the Ro-Theme team (2026-10-08): the previous fixed 50 % mix gave 2.96 / 4.20 contrast with the Ro palette, below 4.5.
- Selected rows and items with a custom text color are unchanged (upstream behavior).
- Override considered: yes. Upstream hard-codes a 70 % text/base mix; a color scheme cannot change the ratio.
- Upstreamable: possibly; not proposed yet.
- Verification: built against v26.08.1 + 0001-0005; RoLight secondary columns #5B5C60 (scheme ForegroundInactive), RoDark about #A3A4A7; selected row text unchanged.
- Upgrade risk: low.
