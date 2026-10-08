# Ro-Theme handoff for the Dolphin design

Status: open. Items below are part of the Ro-ASD Dolphin design but are drawn by the Qt style, color scheme, icon theme, fonts or KWin, not by Dolphin. They belong to Ro-Theme (see AGENTS.md ownership rules). Colors were sampled from the design mockups (2026-10-01).

## 1. Color scheme

Colors come from the Ro-Theme color schemes (`RoLight`, `RoDark`). The hex values measured from the early mockups (#0081ff etc.) are retired; Ro-KDE-Dolphin does not hard-code palette colors. Dolphin reads these roles:

| Role | Used for |
| --- | --- |
| Selection | selected rows and cards, active toolbar toggle |
| View background / alternate | file list background, zebra rows in details view |
| View inactive text (`ForegroundInactive`) | Modified, Size, Type columns (patch 0006) |
| Button vs Window (Header group in the toolbar) | back/forward pill (patch 0007; falls back to window + 14 % text when equal) |
| View background + 7 % text | icon / compact view cards (patches 0008, 0009) |

Open points reported to Ro-Theme (2026-10-08):

- RoDark `[Colors:View]` BackgroundAlternate equals BackgroundNormal (43,43,44), so zebra rows are invisible in dark mode.
- In the toolbar (Plasma Header group) Button equals Window, so the pill uses the fallback tone; a distinct header button tone would let it use the scheme color directly.
- Selection turns very light when the file list loses focus (inactive palette / style); `ChangeSelectionColor=false` did not change it.
- The palette values in the team message differ from the `.colors` files on main; the files are what Dolphin uses.

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
