# Ro-Theme handoff for the Dolphin design

Status: open. Items below are part of the Ro-ASD Dolphin design but are drawn by the Qt style, color scheme, icon theme, fonts or KWin, not by Dolphin. They belong to Ro-Theme (see AGENTS.md ownership rules). Colors were sampled from the design mockups (2026-10-01).

## 1. Color scheme

| Role | Light | Dark | Used for |
| --- | --- | --- | --- |
| Accent / Highlight | #0081ff | #0081ff | selection, active toolbar button, current breadcrumb segment, selected sidebar item |
| Highlighted text | #ffffff | #ffffff | text on accent |
| Window (header, sidebar) | #ffffff | #282828 | toolbar row and Places panel |
| View / Base (content) | #f8f8f8 | #252525 | file list background |
| Alternate base (zebra) | #ededed | #2e2e2e | every other row in details view |
| Text | #1a1a1a | #e6e6e6 | primary text |
| Inactive / secondary text | #8c8c8c | #8a8a8a | section labels, status text (columns are mixed by Dolphin patch 0006) |
| Button background (nav pill) | #e5e5e5 | #444444 | back/forward group |
| Card surface | – | #323232 | home page cards (Ro-KDE-Dolphin will draw them, but should read the palette) |
| Separator | – | #333333 | status bar top border |

Usage bars on the home page use #228af1, #fab33f, #8e6ef7, #34bf76 on a #4b4b4b track (dark).

## 2. Qt style (widget drawing)

- Selection: solid accent fill with highlighted text, small corner radius, no outline or translucent overlay (Breeze draws a translucent frame today).
- Active toggle tool buttons (current view mode): solid accent fill, white icon, rounded rect.
- Places panel: selected item as filled accent rounded rect with bold text; no hover frame.
- Details view header (`CE_Header`): no borders or column separators, same background as the view, text in primary color, sort arrow small.
- Tree branches (`PE_IndicatorBranch`): chevron only (› closed, ˅ open), no dotted or solid tree lines.
- Item hover: no "+" selection marker overlay in icon view (to be confirmed: may be a Dolphin setting rather than style).
- Status bar: flat, separated by a 1 px top line.

## 3. Icons

- Monochrome outline icon set for toolbar, Places panel and file types (folder filled, files outline), as in the mockups.
- App icon: blue rounded square with white folder (may belong to ro-asd-branding).

## 4. Window

- Single header row: titlebar visually merged with the toolbar (same color, no separator line). KWin cannot place window buttons inside the Dolphin toolbar; Ro-Theme decoration should make the titlebar and toolbar read as one row.
- Large rounded window corners and a soft shadow.
- Minimize / maximize / close as thin glyphs without button backgrounds.

## 5. Fonts and locale (not Dolphin)

- Font: a clean sans similar to the mockups; size used for measurements was 10 pt-equivalent (text line ~20 px at 100 %).
- Dates show `1.10.2026`; the design shows `01.10.2026`. Comes from the system locale format (ro-asd-defaults).
- Some MIME type names are untranslated in Turkish ("Folder", "Plain text document"); they come from shared-mime-info, not Dolphin.

## Already handled in Ro-KDE-Dolphin

Toolbar layout, defaults, folder size "—", status bar layout and text, row height and tree indent, secondary column gray (patches 0001–0006, overrides/kxmlgui).
