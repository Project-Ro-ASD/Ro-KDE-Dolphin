## 0001-dolphin-show-dash-for-disabled-folder-size

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7)
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/kitemviews/kfileitemlistwidget.cpp
- Layer: UI only. Changes the text shown in the size column; no KIO, file operation or admin logic is touched.
- Reason (Ro-ASD): the design shows "—" in the size column for folders. Upstream shows an empty cell when folder sizes are disabled.
- Requires: dolphinrc [ContentDisplay] DirectorySizeMode=None (see docs/proposals/dolphinrc-defaults.md). With other modes behavior is unchanged.
- Override considered: yes. No setting or translation can put text into an empty cell.
- Upstreamable: possibly, as an option. Not proposed yet.
- Verification: built against v26.08.1 with cmake/ninja, ran build/bin/dolphin with DirectorySizeMode=None in details view; folders show "—", file sizes unchanged.
- Upgrade risk: low. Check that the size role block in KFileItemListWidgetInformant::roleText still matches on the next Dolphin release.
