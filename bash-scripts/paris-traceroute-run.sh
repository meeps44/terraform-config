#!/usr/bin/env bash

date=$(date '+%Y-%m-%d')
# date=$(date '+%Y-%m-%d %H:%M:%S')
host="$HOSTNAME"
# flow_labels=(0, 23, 100, 150, 200)
flow_labels=(23, 100)
# destination_port="default"

for flow_label in "${flow_labels[@]}"; do
    filename="$HOSTNAME-${date}-${flow_label}.txt"
    echo $filename

    cat file.txt | while read line; do
        destination_address=$line
        sudo paris-traceroute -T $flow_label $destination_address >> $filename
    done

done