## 0006-dolphin-dimmer-secondary-columns

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: v26.08.1 (da98e98d3e806c1ea57edc8e39988173a6dfdef7), applied after 0001-0005
- Fedora 44 package version checked: dolphin-26.08.1-1.fc44
- Affected upstream files:
  - src/kitemviews/kstandarditemlistwidget.cpp (updateAdditionalInfoTextColor)
- Layer: UI color mix only.
- Reason (Ro-ASD): secondary columns (Modified, Size, Type) are mixed from text and base color. Design values (dark: text #e6e6e6, secondary #8a8a8a on #252525; light: #1a1a1a, #8c8c8c on #f8f8f8) correspond to about 50% text, upstream uses 70%.
- Selected rows are unchanged: they still use the highlighted text color.
- Override considered: yes. The ratio is hard-coded; a color scheme can only change the input colors.
- Upstreamable: no, design-specific.
- Verification: built against v26.08.1 + 0001-0005; secondary columns visibly dimmer than the name column, selected row text unchanged.
- Upgrade risk: low.
