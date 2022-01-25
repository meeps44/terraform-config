#!/usr/bin/env bash

date=$(date '+%Y-%m-%d %H:%M:%S')
host="$HOSTNAME"
filename="$HOSTNAME-$date"
flow_label=23
# destination_port="default"

cat file.txt | while read line; do
  echo $line
  destination_address=$line
  sudo paris-traceroute -T $flow_label $destination_address >> $filename.txt
done