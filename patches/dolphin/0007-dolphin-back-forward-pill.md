## 0007-dolphin-back-forward-pill

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0006
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/dolphinmainwindow.cpp (new toolbar action ro_go_back_forward)
- Layer: UI only. Adds a QWidgetAction that shows the existing go_back/go_forward actions as two tool buttons on one rounded background. Navigation logic, shortcuts and history menus are the upstream actions; nothing else changes.
- Reason (Ro-ASD): the design groups back and forward in one pill. KToolBar draws every action separately and has no grouping option.
- Color: window color mixed with 14 % window text (design: #282828 -> #444444 dark, #ffffff -> #e5e5e5 light), so it is visible with any color scheme including Breeze, where Button equals Window.
- Used by: overrides/kxmlgui/dolphinui.rc (go_back + go_forward replaced by ro_go_back_forward). Without the override Dolphin keeps the stock buttons.
- Translations: action text "Back and Forward" in domain ro-kde-dolphin.
- Override considered: yes. A ui.rc cannot group buttons; a style could, but only for every application.
- Upstreamable: no, design-specific.
- Verification: built against v26.08.1 + 0001-0006, Breeze Dark; pill visible, enabled/disabled state follows history, long press opens history menu, Alt+Left/Alt+Right work.
- Upgrade risk: low. Check the back/forward setup in DolphinMainWindow::setupActions on the next Dolphin release.
