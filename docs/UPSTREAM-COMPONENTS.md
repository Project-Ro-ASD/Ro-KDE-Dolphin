# Upstream component map

| Area | Upstream project | Local path |
| --- | --- | --- |
| Dolphin application UI | KDE dolphin (`system/dolphin`) | `patches/dolphin/` |
| Optional Dolphin plugins | KDE dolphin-plugins (`system/dolphin-plugins`) | `patches/dolphin-plugins/` |

Not mapped on purpose:

- KDE Frameworks `kio`: file operations and Places model are shared by every KDE application and file dialog. Changes there are out of scope for this component.

Release cycle: Dolphin is part of KDE Gear. Tags look like `v26.08.1`. The Fedora 44 package version decides which tag a patch is based on.

Do not add a patch until its real upstream owner is confirmed.

For every patch, document (see `docs/PATCH-PROVENANCE-TEMPLATE.md`):

- upstream repository
- upstream file(s)
- upstream commit/tag used while creating the patch
- Ro-ASD reason for the change
- whether an override or upstreamable solution was considered
- test/verification notes
