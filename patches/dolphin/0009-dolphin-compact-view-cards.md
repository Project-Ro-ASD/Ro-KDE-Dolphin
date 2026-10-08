## 0009-dolphin-compact-view-cards

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0008
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/kitemviews/kstandarditemlistwidget.cpp (card drawing from 0008 extended to the compact layout)
  - src/views/dolphinitemlistview.cpp (inner padding 6 px for the compact layout)
- Layer: UI drawing and spacing only.
- Reason (Ro-ASD): same card language as the icon view (0008), derived from the design's folder cards.
- Radius: same 8 px as 0008 (set there). Cards follow each item's own width (chip look), on purpose.
- Depends on: 0008 (the card drawing code it extends).
- Override considered: yes, same as 0008.
- Upstreamable: no, design-specific.
- Verification: built against v26.08.1 + 0001-0008, Breeze Dark; compact items on rounded cards with a small gap, long names not clipped, icon and details views unchanged.
- Upgrade risk: low.
