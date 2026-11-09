#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)

# Regenerate the files in a temp location
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

cd "$TEMP_DIR"
python3 "$SCRIPT_DIR/make-where.py" > /dev/null 2>&1

# Compare the regenerated files against committed ones
cd "$SCRIPT_DIR"
for i in {01..27}; do
    if ! diff -q "$TEMP_DIR/$i-where.svg" "$SCRIPT_DIR/$i-where.svg" > /dev/null 2>&1; then
        echo "Error: Regenerated $i-where.svg differs from committed version"
        exit 1
    fi
done

# Check that each unit page references its image exactly once
cd "$REPO_ROOT"
for i in {01..27}; do
    file_pattern="units/$(printf '%02d' $i)-*/README.md"
    ref_pattern="$i-where\.svg"

    # Find the README file for this unit
    readme_file=$(ls $file_pattern 2>/dev/null | head -1)
    if [ -z "$readme_file" ]; then
        echo "Error: Could not find README for unit $i"
        exit 1
    fi

    # Check it references the right SVG exactly once
    count=$(grep -c "$ref_pattern" "$readme_file" 2>/dev/null || echo 0)
    if [ "$count" -ne 1 ]; then
        echo "Error: Unit $i page references $ref_pattern $count times (expected 1)"
        exit 1
    fi
done

echo "Check passed: all files current and unit pages have proper references"
exit 0
