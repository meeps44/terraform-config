#!/usr/bin/env bash

#hosts=("ubuntu-lon1-0" "ubuntu-ams3-0") # bash array of strings (hostnames)

# date=$(date '+%Y-%m-%d')
#hostname="$HOSTNAME"
# flow_labels=(0 23 100 150 200)
flow_labels=(23 100)
# destination_port="default"

for flow_label in "${flow_labels[@]}"; do

    cat /root/ipv6-address-list.txt | while read line; do
        date=$(date '+%Y-%m-%d-%H:%M:%S')
        filename="$HOSTNAME-${date}-${flow_label}.txt"
        echo "filename: $filename"
        destination_address=$line
        sudo paris-traceroute -T "${flow_label}" "${destination_address}" >> $filename
        grep -o -E "((([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])) | \* \* \*)" $filename > $filename
        #python3 /root/file-to-list.py ${filename} # run script and get json-file. json-file is then sent to logserver via scp
        python3 file-to-list.py ${filename} # run script and get json-file. json-file is then sent to logserver via scp
        # on logserver we can then compare the files and log the result of the comparison
        scp -i ~/.ssh/scp-key ${filename} 209.97.138.74:/root/logs/${HOSTNAME}/
    done
done

# TODO: send $filename to log server via scp
