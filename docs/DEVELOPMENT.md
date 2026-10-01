# Development workflow

## Goal

Development happens against clean upstream KDE checkouts while this repository stores only the Ro-ASD delta. Upstream source trees live under .work/upstream/ and are ignored by Git.

## 1. Check the workstation

    bash scripts/check-env.sh

The script does not install packages or change the system. It only reports the tools that are available.

## 2. Fetch the required KDE upstream

    bash scripts/fetch-upstream.sh list
    bash scripts/fetch-upstream.sh dolphin

The checkout is created at .work/upstream/dolphin. Running the command again performs a fetch/prune instead of creating a second copy.

## 3. Match the Fedora 44 version

Do not patch upstream master blindly. Find the shipped version first:

    rpm -q dolphin
    # or, on a build host
    dnf repoquery --releasever=44 dolphin

Then check out the matching tag in the upstream checkout:

    git -C .work/upstream/dolphin checkout vXX.YY.Z

## 4. Discover before patching

For every requested customization:
1. reproduce or locate the current behavior
2. identify the owning upstream repository
3. identify the exact source, rc or kcfg file
4. check whether an override path exists (kxmlgui, service menu, kcfg default, translation)
5. confirm the change stays in the UI layer (see docs/ARCHITECTURE.md)
6. patch only if the override path is insufficient

Do not copy upstream source files into this repository merely to edit them.

## 5. Create a patch

Edit inside .work/upstream/dolphin on a local branch, commit there, then export:

    git -C .work/upstream/dolphin format-patch -1 -o ../../../patches/dolphin/

Rename the file to the ordered form `NNNN-dolphin-short-description.patch` and add the provenance note from docs/PATCH-PROVENANCE-TEMPLATE.md.

## 6. Validate

    python3 scripts/validate.py

Add targeted tests as real customizations enter the repository.

## Release work

RPM spec, producer manifest and trusted release workflow are intentionally deferred until the repository has a concrete installable payload. Do not invent empty release artifacts.
