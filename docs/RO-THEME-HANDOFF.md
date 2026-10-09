# Ro-Theme handoff for the Dolphin design

Status: open. Items below are part of the Ro-ASD Dolphin design but are drawn by the Qt style, color scheme, icon theme, fonts or KWin, not by Dolphin. They belong to Ro-Theme (see AGENTS.md ownership rules). Last checked against RoLight / RoDark on 2026-10-08.

## Ro-Theme decisions (2026-10-09)

- Qt widget style stays **Breeze**. Some differences (tree lines) will be reduced with Breeze settings; the translucent selection and header separators stay. Section 2 is therefore not planned.
- Accent colors are intentional: the palette is derived from the logo. The mockup accent #0081ff gives 3.76:1 contrast with white text (below 4.5:1); Dolphin uses the scheme accent (#3059A6 light / #7DA2E8 dark). Mockups should be redrawn with Ro colors.
- Icons: the Ro Icons set drawn for Dolphin goes into Ro-Theme `platform/icons/ro-icons` (PR from branch `feat/icons-dolphin`), shipping in Ro-Theme 1.1.0. Ro-Theme adds `[Icons] Theme=ro-icons` to the system and global theme defaults after merge.
- Window decoration: Ro's own Aurorae decoration becomes the default in the window decoration wave; the titlebar uses the window background color. Button shape is decided there.
- Fonts: UI Noto Sans 10 pt, monospace Noto Sans Mono 10 pt, window title Inter semi-bold 10 pt; written to system defaults in a later stage. Cursor stays Breeze; the empty ro-cursor is dropped.
- Theme problems seen in Dolphin are reported as issues in Ro-Theme (screenshot, theme version, app version).

## 1. Color scheme

Colors come from the Ro-Theme color schemes (`RoLight`, `RoDark`). The hex values measured from the early mockups (#0081ff etc.) are retired; Ro-KDE-Dolphin does not hard-code palette colors. Dolphin reads these roles:

| Role | Used for |
| --- | --- |
| Selection | selected rows and cards, active toolbar toggle |
| View background / alternate | file list background, zebra rows in details view |
| View inactive text (`ForegroundInactive`) | Modified, Size, Type columns (patch 0006) |
| Button vs Window (Header group in the toolbar) | back/forward pill (patch 0007; falls back to window + 14 % text when equal) |
| View background + 7 % text | icon / compact view cards (patches 0008, 0009) |

Resolved:

- RoDark zebra rows: `[Colors:View]` BackgroundAlternate is now 50,50,52 (was equal to BackgroundNormal); measured #2B2B2C / #323234 in the details view.
- Selection no longer turns very light when the file list loses focus (`[ColorEffects:Inactive] Enable=false`, `ChangeSelectionColor=false`); checked with the release RPM on 2026-10-08.

Open points reported to Ro-Theme (2026-10-08):

- In the toolbar (Plasma Header group) Button equals Window, so the pill uses the fallback tone; a distinct header button tone would let it use the scheme color directly.
- The palette values in the team message differ from the `.colors` files on main; the files are what Dolphin uses.

## 2. Qt style (widget drawing)

Not planned: Ro-Theme keeps Breeze (see decisions). Kept for reference.

- Selection: solid accent fill with highlighted text, small corner radius, no outline or translucent overlay (Breeze draws a translucent frame today).
- Active toggle tool buttons (current view mode): solid accent fill, white icon, rounded rect.
- Places panel: selected item as filled accent rounded rect with bold text; no hover frame.
- Details view header (`CE_Header`): no borders or column separators, same background as the view, text in primary color, sort arrow small.
- Tree branches (`PE_IndicatorBranch`): chevron only (› closed, ˅ open), no dotted or solid tree lines.
- Status bar: flat, separated by a 1 px top line.

## 3. Icons

- Monochrome outline icon set for toolbar, Places panel and file types (folder filled, files outline), as in the mockups.
- App icon: rounded square in the Ro accent with a white folder.
- Delivered as Ro Icons (Ro-Theme PR `feat/icons-dolphin`, release 1.1.0); icon names Dolphin uses are listed below.

Dolphin ships no icons; it asks the system icon theme for these names (taken from Dolphin 26.08 source). A Ro-Theme icon theme with `Inherits=breeze` in `index.theme` can start with this list and fall back to Breeze for the rest. Monochrome icons should use the `ColorScheme-Text` stylesheet (`currentColor`) as Breeze does, so one set works in RoLight and RoDark.

| Where | Size | Icon names |
| --- | --- | --- |
| Toolbar: back / forward pill | 22 | `go-previous`, `go-next` |
| Toolbar: search | 22 | `edit-find` |
| Toolbar: view modes | 22 | `view-list-icons` (icons), `view-list-tree` (details), `view-list-details` (compact) |
| Toolbar: split | 22 | `view-split-left-right`, `view-right-close` |
| Toolbar: menu | 22 | `application-menu` |
| Places panel (drawn by KIO, check names there) | 16 | `user-home`, `user-desktop`, `folder-documents`, `folder-download`, `folder-music`, `folder-pictures`, `folder-videos`, `user-trash`, `user-trash-full`, `network-workgroup`, `document-open-recent`, `folder-open-recent`, `drive-harddisk`, `drive-removable-media`, `media-optical` |
| File list: folders | 16-22 (details), 48 (icons) | `folder`, `folder-publicshare`, `folder-templates` and the special folders above |
| File list: file types (from shared-mime-info) | 16-22, 48 | `text-plain`, `image-x-generic`, `audio-x-generic`, `video-x-generic`, `application-pdf`, `package-x-generic`, `application-x-rpm`, other MIME icons |
| App icon | all | `org.kde.dolphin` |

Making the icon theme the default (`kdeglobals` `[Icons] Theme=`) belongs to Ro-Theme / ro-asd-defaults, not to Ro-KDE-Dolphin.

## 4. Window

- Single header row: titlebar visually merged with the toolbar (same color, no separator line). KWin cannot place window buttons inside the Dolphin toolbar; Ro-Theme decoration should make the titlebar and toolbar read as one row.
- Large rounded window corners and a soft shadow.
- Planned: Ro Aurorae decoration as default (see decisions).
- Minimize / maximize / close as thin glyphs without button backgrounds.

## 5. Fonts and locale (not Dolphin)

- Font: decided as Noto Sans 10 pt (see decisions). Dolphin draws file names 3 pt larger than the system font (patch 0011).
- Dates show `1.10.2026`; the design shows `01.10.2026`. Comes from the system locale format (ro-asd-defaults).
- Some MIME type names are untranslated in Turkish ("Folder", "Plain text document"); they come from shared-mime-info (upstream), not Dolphin; nobody tracks this yet.

## Already handled in Ro-KDE-Dolphin

Toolbar layout and back/forward pill, defaults, folder size "—", status bar layout and text, row height and tree indent, secondary column gray, icon and compact view cards, no "+" selection marker on hover, larger file names (patches 0001–0011, overrides/kxmlgui).
