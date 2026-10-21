## 0008-dolphin-icon-view-larger-icons-spacing

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0007
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/views/dolphinitemlistview.cpp (inner padding 8 px for the icons layout, 2 px for others as upstream)
  - src/settings/dolphin_iconsmodesettings.kcfg (IconSize default 48, upstream 32)
- Layer: layout spacing and one default. No KIO, file operation or admin logic is touched.
- Reason (Ro-ASD): larger icons and more air between items in the icon view, following the design's folder tiles.
- History: until 0.1.0 this patch also drew a rounded card behind every item (`0008-dolphin-icon-view-cards`). The cards were removed on 2026-10-21 at the team's request (read as a shadow behind the files); selection and hover are drawn by the Qt style as upstream.
- Override considered: yes. IconSize is a KCFG default (team rule: Dolphin-specific defaults are KCFG patches); padding has no setting.
- Upstreamable: no, design-specific.
- Verification: patch series applies to v26.08.1; built and checked on Fedora 44 with RoLight / RoDark.
- Upgrade risk: low. Check DolphinItemListView::updateGridSize on the next Dolphin release.
