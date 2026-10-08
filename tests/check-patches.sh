#!/usr/bin/env bash
# Smoke test: Ro-ASD patches apply in order to the recorded upstream tag,
# the toolbar override is valid XML and the translation catalog compiles.
#
# Usage: bash tests/check-patches.sh
# Env:   DOLPHIN_URL overrides the upstream URL (e.g. a mirror).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

read -r URL TAG < <(python3 -c '
import json
p = json.load(open(".roasd/upstreams.json"))["projects"]["dolphin"]
print(p["url"], p["base_tag"])
')
URL="${DOLPHIN_URL:-$URL}"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo "== upstream: $URL @ $TAG"
git clone --quiet --depth 1 --branch "$TAG" "$URL" "$WORK/dolphin" 2>/dev/null \
  || { echo "cannot clone $URL at $TAG" >&2; exit 2; }

echo "== patches"
count=0
for p in patches/dolphin/*.patch; do
  if ! git -C "$WORK/dolphin" apply --check "$ROOT/$p" 2>"$WORK/err"; then
    echo "FAIL $p" >&2
    cat "$WORK/err" >&2
    exit 1
  fi
  git -C "$WORK/dolphin" apply "$ROOT/$p"
  echo "ok   $p"
  count=$((count + 1))
done
[ "$count" -gt 0 ] || { echo "no patches found" >&2; exit 1; }

echo "== kcfg files still valid XML after patching"
python3 - "$WORK/dolphin/src/settings" <<'PY'
import sys, pathlib, xml.dom.minidom
for f in sorted(pathlib.Path(sys.argv[1]).glob("*.kcfg")):
    xml.dom.minidom.parse(str(f))
print("ok")
PY

echo "== toolbar override"
python3 - <<'PY'
import xml.dom.minidom
d = xml.dom.minidom.parse("overrides/kxmlgui/dolphinui.rc")
names = [a.getAttribute("name") for a in d.getElementsByTagName("ToolBar")[0].getElementsByTagName("Action")]
assert "ro_go_back_forward" in names, "ro_go_back_forward missing from mainToolBar"
print("ok", ", ".join(names))
PY

echo "== translations"
msgfmt --check -o /dev/null overrides/translations/ro-kde-dolphin.po
echo "ok"

echo
echo "All checks passed: $count patches apply to $TAG."
