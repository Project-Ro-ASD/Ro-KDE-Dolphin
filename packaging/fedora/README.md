# Fedora packaging

Delivery model: **rebuilt Dolphin package**. Fedora's `dolphin` source package is rebuilt with the patches in `patches/dolphin/`, the toolbar override and the `ro-kde-dolphin` translation catalog. The package keeps the name `dolphin` and gets the release tag `roasd1` (for example `26.08.1-1.roasd1.fc44`), so it is newer than Fedora's build of the same version.

`apply-ro-asd-spec.py` turns Fedora's unmodified `dolphin.spec` into the Ro-ASD spec. It does not change Fedora's build, test or file lists beyond adding:

- `Patch100…` for every `patches/dolphin/*.patch`, in order
- `Source100` `dolphinui.rc` → `/usr/share/kxmlgui5/dolphin/dolphinui.rc` (not owned by any other package; read before the copy compiled into Dolphin)
- `Source101` `ro-kde-dolphin.po` → `/usr/share/locale/tr/LC_MESSAGES/ro-kde-dolphin.mo` (picked up by `%find_lang --all-name`)
- `BuildRequires: gettext` and a changelog entry

## Local build

    mkdir -p ~/rpmbuild-ro && cd ~/rpmbuild-ro
    dnf download --source dolphin
    rpm -i --define "_topdir $HOME/rpmbuild-ro" dolphin-*.src.rpm
    R=/path/to/Ro-KDE-Dolphin
    cp $R/patches/dolphin/*.patch $R/overrides/kxmlgui/dolphinui.rc $R/overrides/translations/ro-kde-dolphin.po SOURCES/
    python3 $R/packaging/fedora/apply-ro-asd-spec.py SPECS/dolphin.spec
    sudo dnf builddep SPECS/dolphin.spec
    rpmbuild --define "_topdir $HOME/rpmbuild-ro" -ba SPECS/dolphin.spec

Verified 2026-10-08: built from dolphin-26.08.1-1.fc44 and installed as dolphin-26.08.1-1.roasd1.fc44 (replacing Fedora's updates build).

Rollback on a test machine: `sudo dnf downgrade dolphin dolphin-libs`.

## Open (team / Ro-Repo)

1. Who builds and publishes to the Ro-ASD repository, and from where (CI, build host); packages must be signed with the Ro-ASD key.
2. Update policy: when Fedora ships a newer Dolphin (e.g. 26.08.2-1), it is newer than 26.08.1-1.roasd1. Ro-Repo needs repository priority or `excludepkgs=dolphin*` on the Fedora repos, and this repository must rebuild against the new version (patches re-checked first).
3. Whether the `RELEASE_TAG` scheme (`roasd1`, `roasd2`, …) matches Ro-Repo's naming rules.
