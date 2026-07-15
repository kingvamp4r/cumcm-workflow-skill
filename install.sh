#!/usr/bin/env bash

# Install the CUMCM workflow Skill from a tagged GitHub source archive.
# macOS / Linux / Git Bash / WSL only. Native Windows PowerShell is not supported.

set -euo pipefail

REPOSITORY="kingvamp4r/cumcm-workflow-skill"
VERSION="${CUMCM_WORKFLOW_VERSION:-v1demo}"
SKILLS_ROOT="${CUMCM_SKILLS_DIR:-$HOME/.agents/skills}"
DESTINATION="$SKILLS_ROOT/cumcm-workflow"
ARCHIVE_URL="https://github.com/$REPOSITORY/archive/refs/tags/$VERSION.tar.gz"
TEMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

if [ -e "$DESTINATION" ]; then
  printf 'Installation stopped: %s already exists.\n' "$DESTINATION" >&2
  printf 'Choose another CUMCM_SKILLS_DIR or remove that directory first.\n' >&2
  exit 1
fi

command -v curl >/dev/null 2>&1 || {
  printf 'curl is required to install this Skill.\n' >&2
  exit 1
}
command -v tar >/dev/null 2>&1 || {
  printf 'tar is required to install this Skill.\n' >&2
  exit 1
}

printf 'Downloading %s (%s)…\n' "$REPOSITORY" "$VERSION"
curl --fail --location --silent --show-error "$ARCHIVE_URL" --output "$TEMP_DIR/source.tar.gz"
tar -xzf "$TEMP_DIR/source.tar.gz" -C "$TEMP_DIR"

SOURCE_DIR="$(find "$TEMP_DIR" -mindepth 1 -maxdepth 1 -type d -name 'cumcm-workflow-skill-*' -print -quit)"
if [ -z "$SOURCE_DIR" ] || [ ! -f "$SOURCE_DIR/SKILL.md" ]; then
  printf 'The downloaded archive is not a valid CUMCM workflow Skill release.\n' >&2
  exit 1
fi

mkdir -p "$SKILLS_ROOT"
mv "$SOURCE_DIR" "$DESTINATION"

printf 'Installed CUMCM workflow Skill to %s\n' "$DESTINATION"
printf 'Restart Codex, then use $cumcm-workflow in a new conversation.\n'
