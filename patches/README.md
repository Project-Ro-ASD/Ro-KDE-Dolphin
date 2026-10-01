# Patches

Store downstream source patches here, grouped by their KDE upstream repository.

Expected layout:

```text
patches/
  dolphin/
  dolphin-plugins/
```

Patch filenames should be ordered and descriptive, for example:

```text
0001-dolphin-adjust-ro-asd-statusbar-layout.patch
0001-dolphin-adjust-ro-asd-statusbar-layout.md
```

Each patch must have a matching provenance note with the same base name (see `docs/PATCH-PROVENANCE-TEMPLATE.md`). Patches must stay in the Dolphin UI layer.
