# Fedora packaging

## Decisions (team, 2026-10-08)

- **Model:** package-name-preserving downstream rebuild. Fedora 44 Dolphin SRPM/spec → Ro-ASD patches → Ro-ASD rebuilt Dolphin RPM family.
- **RPM names:** Fedora's names are kept: `dolphin`, `dolphin-libs`, `dolphin-devel`. No `ro-kde-dolphin` RPM and no `Provides: dolphin` replacement package. `ro-kde-dolphin` is only the component / repository identity.
- **Versions:** `Version` follows Fedora/upstream Dolphin, `Release` carries the Ro-ASD revision: `26.08.1-1.roasd1.fc44`. The component version (`VERSION`, e.g. `0.1.0`) is separate from the RPM NEVRA.
- **Fedora override:** Ro-Repo producer registry authorises this component with `allow_fedora_override: true` (package_names `dolphin`, `dolphin-libs`, `dolphin-devel`, x86_64, risk_class `critical-desktop`, SRPM required). Handled in Ro-Repo.
- **Update policy:** Ro-ASD repos get a higher DNF `priority` than Fedora (handled in `ro-asd-repos`); no `excludepkgs`. In return this repository must rebase onto every new Fedora Dolphin quickly: new baseline → patch check → build → dependency/upgrade/smoke tests → new release.
- **Build and publish:** trusted GitHub Actions release workflow in this repository (`.github/workflows/release.yml`) builds RPM + SRPM in Fedora 44, runs tests, writes `SHA256SUMS` and `component-artifact-manifest-v1.json`, attests and publishes an immutable GitHub Release. Ro-Repo accepts it, verifies provenance, signs with the central key and promotes. No signing key lives in this repository.

## Files

- `dolphin.spec.fedora`: Fedora's unmodified spec for the current baseline
- `baseline.json`: baseline NEVR and Source0 SHA256
- `apply-ro-asd-spec.py`: turns the baseline into the Ro-ASD spec, adding only:
  - `Patch100…` for every `patches/dolphin/*.patch`, in order
  - `Source100` `dolphinui.rc` → `/usr/share/kxmlgui5/dolphin/dolphinui.rc` (not owned by any Fedora package)
  - `Source101` `ro-kde-dolphin.po` → `/usr/share/locale/tr/LC_MESSAGES/ro-kde-dolphin.mo` (picked up by `%find_lang --all-name`)
  - `BuildRequires: gettext`, the `roasdN` release tag and a changelog entry

`tests/check-spec.sh` (CI) checks that the baseline matches `baseline.json` and `upstreams.json` `base_tag`, and that the generated spec lists every patch.

## Local build

    mkdir -p ~/rpmbuild-ro/{SPECS,SOURCES} && cd ~/rpmbuild-ro
    R=/path/to/Ro-KDE-Dolphin
    cp $R/packaging/fedora/dolphin.spec.fedora SPECS/dolphin.spec
    cp $R/patches/dolphin/*.patch $R/overrides/kxmlgui/dolphinui.rc $R/overrides/translations/ro-kde-dolphin.po SOURCES/
    spectool -g -C SOURCES SPECS/dolphin.spec   # then compare sha256 with baseline.json
    python3 $R/packaging/fedora/apply-ro-asd-spec.py SPECS/dolphin.spec
    sudo dnf builddep SPECS/dolphin.spec
    rpmbuild --define "_topdir $HOME/rpmbuild-ro" -ba SPECS/dolphin.spec

Verified 2026-10-08: dolphin-26.08.1-1.roasd1.fc44 built, installed over Fedora's build and checked on a running system. Rollback on a test machine: `sudo dnf downgrade dolphin dolphin-libs`.

## Rebase onto a new Fedora Dolphin

1. Replace `dolphin.spec.fedora` and `baseline.json` with the new Fedora build.
2. Set `base_tag` in `.roasd/upstreams.json` to the matching upstream tag.
3. Run `bash tests/check-patches.sh`; refresh any patch that fails and update its provenance note.
4. Run `bash tests/check-spec.sh`, build locally, then release.

## Release (Ro-Repo V2 producer)

`.github/workflows/release.yml`, based on `Project-Ro-ASD/ro-Assist`:

- trigger: tag `v<VERSION>` (component version) on main; `workflow_dispatch` = dry run (build and tests, no release)
- Fedora 44 container: patch/spec checks, Source0 SHA256 check, `rpmbuild -ba`, rpmlint (advisory, as in Ro-Repo acceptance), clean install + smoke
- publishes exactly `dolphin`, `dolphin-libs`, `dolphin-devel` (x86_64) and the SRPM; debuginfo/debugsource are not published because they are not in the Ro-Repo `package_names`
- `SHA256SUMS`, `component-artifact-manifest-v1.json` (Ro-Repo schema), GitHub attestation, draft → verify → publish

Requires GitHub release immutability to be enabled for this repository (Ro-Repo checks `immutable == true`).
