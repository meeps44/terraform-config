#!/usr/bin/env bash

# ref: https://stackoverflow.com/questions/20796200/how-to-loop-over-files-in-directory-and-change-path-and-add-suffix-to-filename

directory=$1

for filename in ${directory}/*.json; do
    # [ -e "$filename" ] || continue
    [ python3 /root/git/terraform-config/python-scripts/route-compare.py "$filename" ] || continue
    # ... rest of the loop body
done