#!/usr/bin/env bash

set -euo pipefail

directory="${1:-.}"

if [[ ! -d "$directory" ]]; then
    echo "Papka topilmadi: $directory" >&2
    exit 1
fi

file_count=$(find "$directory" -maxdepth 1 -type f | wc -l)
echo "'$directory' papkasida $file_count ta fayl bor."