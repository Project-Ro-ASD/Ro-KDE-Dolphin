## 0005-dolphin-taller-details-rows-compact-indent

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0004
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/views/dolphinitemlistview.cpp (DolphinItemListView::updateGridSize, details layout)
  - src/kitemviews/kstandarditemlistwidget.cpp (updateExpansionArea, updateDetailsLayoutTextCache, drawSiblingsInformation)
- Layer: UI layout only. No KIO, file operation or admin logic is touched.
- Reason (Ro-ASD): the design uses details rows about twice the line height. Upstream ties tree indentation to the row height, so taller rows would double the indentation; indentation is fixed to icon size + 4 * padding (the upstream value at default row height).
- Row height: padding * 2 + max(icon, lineSpacing) + 3/4 lineSpacing, so it scales with font and display scale.
- Override considered: yes. No setting controls row height; DetailsMode LeftPadding/RightPadding are horizontal only.
- Upstreamable: possibly as a "row spacing" option. Not proposed yet.
- Verification: built against v26.08.1 + 0001-0004; row/line height ratio about 1.95 (design 39/20); text vertically centered; expanded folders indent one icon + 8 px per level.
- Upgrade risk: medium. Four places in kstandarditemlistwidget.cpp; re-check expansion area and sibling drawing on the next Dolphin release.
