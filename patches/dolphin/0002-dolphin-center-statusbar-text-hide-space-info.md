## 0002-dolphin-center-statusbar-text-hide-space-info

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/statusbar/dolphinstatusbar.cpp
- Layer: UI only. Changes label alignment and hides the disk space widget; no KIO, file operation or admin logic is touched.
- Reason (Ro-ASD): the design shows a full-width status bar with only centered text and no disk space indicator.
- Requires: dolphinrc [General] ShowStatusBar=FullWidth (see docs/proposals/dolphinrc-defaults.md). Small and Disabled modes are unchanged.
- Override considered: yes. Dolphin has no setting to hide the space indicator or align the status text.
- Upstreamable: the space indicator part could be proposed as an option. Not proposed yet.
- Verification: built against v26.08.1 + 0001, ran build/bin/dolphin with ShowStatusBar=FullWidth; text centered for summary, hover and selection; no disk space widget.
- Upgrade risk: low. Check DolphinStatusBar constructor (m_label setup) and updateMode() FullWidth case on the next Dolphin release.
