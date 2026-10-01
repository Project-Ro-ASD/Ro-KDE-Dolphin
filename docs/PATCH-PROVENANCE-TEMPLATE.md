# Patch provenance template

Copy this file next to the patch with the same base name and a `.md` extension:

    patches/dolphin/0001-dolphin-example-change.patch
    patches/dolphin/0001-dolphin-example-change.md

`scripts/validate.py` fails if a `.patch` file has no matching `.md` note.

---

## 0001-dolphin-example-change

- Upstream repository: https://invent.kde.org/system/dolphin.git
- Upstream base tag/commit: vXX.YY.Z (commit SHA)
- Fedora 44 package version checked: dolphin-XX.YY.Z-N.fc44
- Affected upstream files:
  - src/...
- Layer: UI only (confirm no KIO / file operation / admin logic is touched)
- Reason (Ro-ASD): ...
- Override considered: yes/no, why it was not enough
- Upstreamable: yes/no, link to KDE merge request or bug if any
- Verification: how it was built and tested, screenshots if visual
- Upgrade risk: low/medium/high, what to check on the next Dolphin release
