# Tests

## check-patches.sh (CI job `patches`)

    bash tests/check-patches.sh

- clones upstream Dolphin at `base_tag` from `.roasd/upstreams.json`
- applies every `patches/dolphin/*.patch` in order and stops at the first one that does not apply
- checks the patched kcfg files, the toolbar override and the translation catalog

When Fedora moves to a new Dolphin version: update `base_tag`, run this script, and refresh any patch that fails before rebuilding the package.

## Not automated yet

- Dolphin launches and opens a folder after package installation
- toolbar, status bar and view changes are visible (checked by hand with screenshots so far)
- basic file operations (copy, move, delete to trash) still work unchanged
