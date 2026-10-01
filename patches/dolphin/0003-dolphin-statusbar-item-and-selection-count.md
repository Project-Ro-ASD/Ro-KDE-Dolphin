## 0003-dolphin-statusbar-item-and-selection-count

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001 and 0002
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/views/dolphinview.cpp (DolphinView::requestStatusBarText)
  - src/dolphinviewcontainer.cpp (DolphinViewContainer::showItemInfo)
- Layer: UI only. Changes the status bar text. The recursive size stat job for the status text is no longer started; no file operation or admin logic is touched.
- Reason (Ro-ASD): the design shows "12 öğe, 1 seçili" (visible items incl. expanded folders, selection count) and no per-item text on hover.
- Translations: new strings use the Ro-ASD translation domain "ro-kde-dolphin" (i18ndp), not Dolphin's own catalog. Turkish is in overrides/translations/ro-kde-dolphin.po; the compiled .mo must be installed as /usr/share/locale/tr/LC_MESSAGES/ro-kde-dolphin.mo by packaging.
- Override considered: yes. Existing Dolphin strings combine into "12 öge, 1 öge seçildi", which does not match the design.
- Upstreamable: no, design-specific.
- Verification: built against v26.08.1 + 0001 + 0002, tr locale, .mo in ~/.local/share/locale; shows "5 öğe" without selection, "5 öğe, 1 seçili" with selection, unchanged while hovering.
- Upgrade risk: medium. requestStatusBarText and showItemInfo are touched; re-check both on the next Dolphin release.
