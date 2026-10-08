#!/usr/bin/env bash
# Smoke test: the recorded Fedora baseline spec turns into a valid Ro-ASD spec.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

BASE=packaging/fedora/dolphin.spec.fedora
[ -f "$BASE" ] || { echo "missing $BASE" >&2; exit 1; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
cp "$BASE" "$WORK/dolphin.spec"

echo "== baseline matches packaging/fedora/baseline.json"
python3 - "$BASE" <<'PY'
import json, re, sys
b = json.load(open("packaging/fedora/baseline.json"))
spec = open(sys.argv[1]).read()
ver = re.search(r"^Version:\s*(\S+)$", spec, re.M).group(1)
rel = re.search(r"^Release:\s*(\d+)%\{\?dist\}$", spec, re.M).group(1)
assert f"dolphin-{ver}-{rel}.fc44" == b["fedora_nevr"], (ver, rel, b["fedora_nevr"])
up = json.load(open(".roasd/upstreams.json"))["projects"]["dolphin"]["base_tag"]
assert up == "v" + ver, f"upstreams.json base_tag {up} does not match spec Version {ver}"
print("ok", b["fedora_nevr"], up)
PY

echo "== generate Ro-ASD spec"
python3 packaging/fedora/apply-ro-asd-spec.py "$WORK/dolphin.spec"

echo "== generated spec content"
python3 - "$WORK/dolphin.spec" <<'PY'
import pathlib, re, sys
spec = open(sys.argv[1]).read()
patches = sorted(p.name for p in pathlib.Path("patches/dolphin").glob("*.patch"))
listed = re.findall(r"^Patch\d+:\s*(\S+)$", spec, re.M)
assert listed == patches, f"Patch lines {listed} != {patches}"
assert re.search(r"^Release:\s*\d+\.roasd\d+%\{\?dist\}$", spec, re.M), "Release has no roasd tag"
for s in ("Source100:      dolphinui.rc", "Source101:      ro-kde-dolphin.po",
          "%{_kf6_datadir}/kxmlgui5/dolphin/dolphinui.rc", "ro-kde-dolphin.mo"):
    assert s in spec, f"missing: {s}"
print("ok", len(listed), "patches")
PY

echo
echo "Spec check passed."
