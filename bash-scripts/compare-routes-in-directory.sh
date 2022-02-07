#!/usr/bin/env bash

# ref: https://stackoverflow.com/questions/20796200/how-to-loop-over-files-in-directory-and-change-path-and-add-suffix-to-filename

directory=$1
# comparator = the base file we want to compare against
comparator=$2

for filename in ${directory}/*.json; do
    # Check if file exists, if yes continue:
    [ -e "$filename" ] || continue
    # Run command
    python3 /root/git/terraform-config/python-scripts/route-compare.py "$comparator" "$filename"
done
