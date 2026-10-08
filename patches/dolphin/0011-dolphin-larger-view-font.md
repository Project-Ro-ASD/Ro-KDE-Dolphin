## 0011-dolphin-larger-view-font

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0010
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/views/dolphinitemlistview.cpp (DolphinItemListView::updateFont)
- Layer: UI font size only, file views (details, icons, compact). Sidebar, toolbar and menus are unchanged.
- Reason (Ro-ASD): team feedback that file names were too small. When the view uses the system font (default), it is used 3 points larger (10 pt -> 13 pt). Row height (0005) and cards (0008/0009) scale with it. A custom view font chosen in Dolphin's settings is used as is.
- Override considered: raising the system font would change every application (Ro-Theme / ro-asd-defaults scope); this keeps the change Dolphin-only.
- Upstreamable: no, distribution-specific.
- Verification: built against v26.08.1 + 0001-0010, RoDark; file names visibly larger in all three views. Users with manually resized columns may need to widen them; automatic column widths follow the font.
- Upgrade risk: low.
