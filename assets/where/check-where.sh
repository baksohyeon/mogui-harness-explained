#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)

# Regenerate the files in a temp location
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

python3 "$SCRIPT_DIR/make-where.py" "$TEMP_DIR" > /dev/null 2>&1

# Compare all 27 files against committed ones
DIFF_COUNT=0
for i in $(seq -w 1 27); do
    if ! diff -q "$TEMP_DIR/$i-where.svg" "$SCRIPT_DIR/$i-where.svg" > /dev/null 2>&1; then
        DIFF_COUNT=$((DIFF_COUNT + 1))
    fi
done

if [ $DIFF_COUNT -gt 0 ]; then
    echo "Error: $DIFF_COUNT regenerated files differ from committed versions"
    exit 1
fi

# Check that each unit page references its image exactly once
cd "$REPO_ROOT"
for i in $(seq -w 1 27); do
    readme_file=$(ls units/$(printf '%02d' $((10#$i)))-*/README.md 2>/dev/null | head -1)
    if [ -z "$readme_file" ]; then
        echo "Error: Could not find README for unit $i"
        exit 1
    fi

    ref_pattern="$i-where\.svg"
    count=$(grep -c "$ref_pattern" "$readme_file" 2>/dev/null || echo 0)
    if [ "$count" -ne 1 ]; then
        echo "Error: Unit $i page references $ref_pattern $count times (expected 1)"
        exit 1
    fi
done

echo "Check passed: all files current and unit pages have proper references"
exit 0
