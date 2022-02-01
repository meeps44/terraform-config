#!/usr/bin/env bash

# date=$(date '+%Y-%m-%d')
date=$(date '+%Y-%m-%d %H:%M:%S')
host="$HOSTNAME"
# flow_labels=(0 23 100 150 200)
flow_labels=(23 100)
# destination_port="default"

for flow_label in "${flow_labels[@]}"; do

    cat ipv6-address-list.txt | while read line; do
        filename="$HOSTNAME-${date}-${flow_label}.txt"
        echo "filename: $filename"
        destination_address=$line
        sudo paris-traceroute -T $flow_label $destination_address >> $filename
    done
    python3 file-to-list.py $filename # run script and get json-file. json-file is then sent to logserver via scp
    # on logserver we can then compare the files and log the result of the comparison
    scp -i ~/.ssh/scp-key $filename 209.97.138.74:/root/logs/test-logs-january/
done

# TODO: send $filename to log server via scp
