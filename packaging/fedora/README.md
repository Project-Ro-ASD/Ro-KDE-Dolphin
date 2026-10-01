# Fedora packaging

This directory will contain the RPM spec and source preparation required to ship Ro-KDE-Dolphin on the Ro-ASD Fedora base.

Two delivery models are possible and must be decided before the first release:

1. Override-only package: installs kxmlgui, service menu and translation files without replacing files owned by the `dolphin` package.
2. Rebuilt Dolphin package: rebuilds Fedora's `dolphin` source RPM with the patches in `patches/dolphin/` applied. Required as soon as any source patch exists.

Before the first RPM release, define:

1. delivery model (override-only or rebuilt package)
2. exact installed file ownership
3. required dolphin / KDE Gear package versions
4. patch application order
5. upgrade/rollback behavior when Fedora ships a newer Dolphin
6. Ro-Repo producer/release integration
