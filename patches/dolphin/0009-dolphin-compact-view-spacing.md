## 0009-dolphin-compact-view-spacing

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0008
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/views/dolphinitemlistview.cpp (inner padding 6 px for the compact layout)
- Layer: spacing only.
- Reason (Ro-ASD): same spacing language as the icon view (0008).
- History: until 0.1.0 this patch also drew cards in the compact view (`0009-dolphin-compact-view-cards`); removed on 2026-10-21 together with 0008's cards.
- Depends on: 0008 (padding line it extends).
- Override considered: yes, same as 0008.
- Upstreamable: no, design-specific.
- Verification: patch series applies to v26.08.1; compact items keep a small gap, long names not clipped.
- Upgrade risk: low.
