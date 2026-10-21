## 0012-dolphin-context-menu-quick-row-more-options

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0011
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/dolphincontextmenu.cpp (item and viewport context menus; trash menus unchanged)
  - src/dolphincontextmenu.h (two helpers take a target menu; one new private helper)
- Layer: menu layout only. Every entry is an existing Dolphin, KIO or plugin action, triggered exactly as before. No KIO, file operation or admin logic is touched; nothing is removed.
- Reason (Ro-ASD): design "B" chosen on 2026-10-21 (Ro-KDE-Dolphin context menu mockups):
  - Item menu (files, folders, multiple selection): a row of four large buttons on top (Cut, Copy, Rename, Move to Trash, or Delete / the Shift-aware remove action exactly as upstream chooses), then the open group (new tab, new window, split view, open with), then Create New, Copy Location, Paste, Duplicate Here, Add to Places (and Delete when both trash and delete are shown), Copy To / Move To when enabled, then "More Options" (plugins: actions, activities, tags, compress, open as administrator; open terminal for folders; version control), then Properties.
  - Empty area menu: buttons for New Folder, Paste (disabled when there is nothing to paste), Terminal (only where upstream offers it) and Hidden Files (toggle), then Create New, View Mode, Sort By, then "More Options" (open with, Add to Places, plugins, version control), then Properties.
- The buttons mirror their actions (icon, enabled and checked state, shortcut in the tooltip) and close the menu before triggering. The button tile is window color mixed with 7 % text, so it follows any color scheme. "More Options" is only added when it has entries.
- Strings: short button labels and "More Options" in the ro-kde-dolphin domain (overrides/translations).
- Override considered: yes. Dolphin's context menu settings can only hide some entries; grouping and the button row need code.
- Upstreamable: no, design-specific.
- Verification: patch series applies to v26.08.1; build and menus checked with the release workflow dry run and on Fedora 44.
- Upgrade risk: medium. dolphincontextmenu.cpp changes often upstream; re-check addItemContextMenu, addViewportContextMenu, insertDefaultItemActions and addAdditionalActions on every rebase.
