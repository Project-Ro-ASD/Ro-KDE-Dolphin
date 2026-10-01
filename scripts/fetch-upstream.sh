#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE="$ROOT/.work/upstream"
mkdir -p "$WORKSPACE"

# Single source of truth: .roasd/upstreams.json
declare -A URLS=()
while IFS='=' read -r name url; do
  URLS["$name"]="$url"
done < <(python3 -c '
import json, sys
data = json.load(open(sys.argv[1]))
for name, project in data["projects"].items():
    print(name + "=" + project["url"])
' "$ROOT/.roasd/upstreams.json")

list_projects() {
  printf "%s\n" "${!URLS[@]}" | sort
}

fetch_project() {
  local project="$1"
  local url="${URLS[$project]:-}"
  local dest="$WORKSPACE/$project"

  if [[ -z "$url" ]]; then
    echo "Unknown upstream project: $project" >&2
    echo "Known projects:" >&2
    list_projects >&2
    exit 2
  fi

  if [[ -d "$dest/.git" ]]; then
    current="$(git -C "$dest" remote get-url origin)"
    if [[ "$current" != "$url" ]]; then
      echo "Refusing to update $dest: origin is $current, expected $url" >&2
      exit 3
    fi
    echo "Updating $project..."
    git -C "$dest" fetch --tags --prune origin
  elif [[ -e "$dest" ]]; then
    echo "Refusing to overwrite non-git path: $dest" >&2
    exit 4
  else
    echo "Cloning $project..."
    git clone "$url" "$dest"
  fi

  echo
  echo "$project workspace: $dest"
  echo "HEAD: $(git -C "$dest" rev-parse HEAD)"
  echo "Branch: $(git -C "$dest" branch --show-current || true)"
  echo "Latest tags: $(git -C "$dest" tag --sort=-creatordate | head -3 | tr '\n' ' ')"
}

case "${1:-}" in
  list)
    list_projects
    ;;
  all)
    while IFS= read -r project; do
      fetch_project "$project"
      echo
    done < <(list_projects)
    ;;
  "")
    echo "Usage: bash scripts/fetch-upstream.sh <project|all|list>" >&2
    exit 2
    ;;
  *)
    fetch_project "$1"
    ;;
esac
