#!/usr/bin/env python3
"""Turn Fedora's dolphin.spec into the Ro-ASD rebuild spec.

Usage: python3 packaging/fedora/apply-ro-asd-spec.py <path/to/dolphin.spec>

Adds the Ro-KDE-Dolphin patches (patches/dolphin/*.patch, in order), the
toolbar override (overrides/kxmlgui/dolphinui.rc) and the ro-kde-dolphin
translation catalog. Fedora's own build steps are left untouched.
The spec is edited in place; run it on a fresh copy of Fedora's spec.
"""
from pathlib import Path
from datetime import date
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RELEASE_TAG = "roasd1"


def rpm_date():
    # RPM changelog dates must be English, independent of the user's locale.
    d = date.today()
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{days[d.weekday()]} {months[d.month - 1]} {d.day:02d} {d.year}"


def replace_once(text, old, new):
    if text.count(old) != 1:
        sys.exit(f"spec layout not recognised, expected exactly one: {old.strip()!r}")
    return text.replace(old, new)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    spec_path = Path(sys.argv[1])
    spec = spec_path.read_text()
    if "Ro-ASD" in spec:
        sys.exit("spec already contains Ro-ASD changes; start from Fedora's original spec")

    patches = sorted((ROOT / "patches" / "dolphin").glob("*.patch"))
    if not patches:
        sys.exit("no patches found in patches/dolphin")

    # Release: keep Fedora's number, add a Ro-ASD tag
    spec, n = re.subn(r"^(Release:\s*)(\d+)(%\{\?dist\})$", rf"\g<1>\g<2>.{RELEASE_TAG}\g<3>", spec, count=1, flags=re.M)
    if n != 1:
        sys.exit("Release line not recognised")

    # Sources and patches
    lines = ["", "# Ro-ASD (Ro-KDE-Dolphin): toolbar override and translation catalog",
             "Source100:      dolphinui.rc",
             "Source101:      ro-kde-dolphin.po",
             "# Ro-ASD (Ro-KDE-Dolphin): downstream UI patches, see patches/dolphin/*.md"]
    for i, p in enumerate(patches, start=100):
        lines.append(f"Patch{i}:       {p.name}")
    spec = replace_once(spec, "# Upstream\n", "# Upstream\n" + "\n".join(lines) + "\n")

    spec = replace_once(spec, "BuildRequires:  desktop-file-utils\n",
                        "BuildRequires:  desktop-file-utils\nBuildRequires:  gettext\n")

    # Install the override and the compiled catalog before %find_lang picks up translations
    spec = replace_once(spec, "%cmake_install\n",
                        "%cmake_install\n"
                        "# Ro-ASD: toolbar layout (overrides the copy compiled into Dolphin)\n"
                        "install -Dpm 0644 %{SOURCE100} %{buildroot}%{_kf6_datadir}/kxmlgui5/dolphin/dolphinui.rc\n"
                        "# Ro-ASD: strings added by Ro-ASD patches (domain ro-kde-dolphin)\n"
                        "install -d %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES\n"
                        "msgfmt %{SOURCE101} -o %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/ro-kde-dolphin.mo\n")

    spec = replace_once(spec, "%{_kf6_datadir}/zsh/site-functions/_dolphin\n",
                        "%{_kf6_datadir}/zsh/site-functions/_dolphin\n"
                        "%dir %{_kf6_datadir}/kxmlgui5/dolphin\n"
                        "%{_kf6_datadir}/kxmlgui5/dolphin/dolphinui.rc\n")

    # Changelog entry
    m = re.search(r"^Version:\s*(\S+)$", spec, flags=re.M)
    rel = re.search(r"^Release:\s*(\S+?)%\{\?dist\}$", spec, flags=re.M)
    entry = (f"* {rpm_date()} Ro-ASD <contact@roasd.org> - {m.group(1)}-{rel.group(1)}\n"
             f"- Ro-ASD UI patches 0001-{len(patches):04d}, toolbar override and ro-kde-dolphin translations\n\n")
    spec, n = re.subn(r"^%changelog\n", lambda _: "%changelog\n" + entry, spec, count=1, flags=re.M)
    if n != 1:
        sys.exit("%changelog section not recognised")

    spec_path.write_text(spec)
    print(f"{spec_path}: {len(patches)} patches, release tag {RELEASE_TAG}")


if __name__ == "__main__":
    main()
