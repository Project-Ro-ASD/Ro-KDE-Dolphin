## 0008-dolphin-icon-view-cards

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0007
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/kitemviews/kstandarditemlistwidget.cpp (KStandardItemListWidget::paint, icons layout only)
  - src/views/dolphinitemlistview.cpp (inner padding 8 px for the icons layout, 2 px for others as upstream)
  - src/settings/dolphin_iconsmodesettings.kcfg (IconSize default 48, upstream 32)
- Layer: UI drawing, layout spacing and one default. No KIO, file operation or admin logic is touched.
- Reason (Ro-ASD): the design's folder cards (rounded tiles, icon centered, name below) are applied to the existing icon view instead of a separate home page (team decision 2026-10-08).
- Card color: base mixed with 7 % text (design: #252525 -> #323232), so it follows any color scheme. Radius 8 px from the Ro radius scale 4/8/12/18/24 (Ro-Theme decision), clamped to half the card height.
- Card aspect is kept wider than the mockup on purpose: the mockup showed six cards on a home page; a file view needs more items per screen.
- Override considered: yes. No setting draws item backgrounds; a Qt style would affect every application.
- Upstreamable: no, design-specific.
- Verification: built against v26.08.1 + 0001-0007, Breeze Dark; cards visible, selection and hover drawn on top, zoom scales cards, details and compact views unchanged.
- Upgrade risk: low. Check the start of KStandardItemListWidget::paint and DolphinItemListView::updateGridSize on the next Dolphin release.
