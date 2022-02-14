import json, uuid, argparse, datetime, os, re, subprocess, ipaddress

IPV4SEG  = r'(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])'
IPV4ADDR = r'(?:(?:' + IPV4SEG + r'\.){3,3}' + IPV4SEG + r')'
IPV6SEG  = r'(?:(?:[0-9a-fA-F]){1,4})'
IPV6GROUPS = (
    r'(?:' + IPV6SEG + r':){7,7}' + IPV6SEG,                  # 1:2:3:4:5:6:7:8
    r'(?:' + IPV6SEG + r':){1,7}:',                           # 1::                                 1:2:3:4:5:6:7::
    r'(?:' + IPV6SEG + r':){1,6}:' + IPV6SEG,                 # 1::8               1:2:3:4:5:6::8   1:2:3:4:5:6::8
    r'(?:' + IPV6SEG + r':){1,5}(?::' + IPV6SEG + r'){1,2}',  # 1::7:8             1:2:3:4:5::7:8   1:2:3:4:5::8
    r'(?:' + IPV6SEG + r':){1,4}(?::' + IPV6SEG + r'){1,3}',  # 1::6:7:8           1:2:3:4::6:7:8   1:2:3:4::8
    r'(?:' + IPV6SEG + r':){1,3}(?::' + IPV6SEG + r'){1,4}',  # 1::5:6:7:8         1:2:3::5:6:7:8   1:2:3::8
    r'(?:' + IPV6SEG + r':){1,2}(?::' + IPV6SEG + r'){1,5}',  # 1::4:5:6:7:8       1:2::4:5:6:7:8   1:2::8
    IPV6SEG + r':(?:(?::' + IPV6SEG + r'){1,6})',             # 1::3:4:5:6:7:8     1::3:4:5:6:7:8   1::8
    r':(?:(?::' + IPV6SEG + r'){1,7}|:)',                     # ::2:3:4:5:6:7:8    ::2:3:4:5:6:7:8  ::8       ::
    r'fe80:(?::' + IPV6SEG + r'){0,4}%[0-9a-zA-Z]{1,}',       # fe80::7:8%eth0     fe80::7:8%1  (link-local IPv6 addresses with zone index)
    r'::(?:ffff(?::0{1,4}){0,1}:){0,1}[^\s:]' + IPV4ADDR,     # ::255.255.255.255  ::ffff:255.255.255.255  ::ffff:0:255.255.255.255 (IPv4-mapped IPv6 addresses and IPv4-translated addresses)
    r'(?:' + IPV6SEG + r':){1,4}:[^\s:]' + IPV4ADDR,          # 2001:db8:3:4::192.0.2.33  64:ff9b::192.0.2.33 (IPv4-Embedded IPv6 Address)
)
IPV6ADDR = '|'.join(['(?:{})'.format(g) for g in IPV6GROUPS[::-1]])  # Reverse rows for greedy match

file = "/home/erlend/git/terraform-config/python-scripts/example-output/example-output-1.txt"
flow_label_list = []
reg = r"((([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+([0-9a-fA-F]+))+"
pattern = re.compile(reg)

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("hostname")
parser.add_argument("tcp_port")
parser.add_argument("source_ip")
parser.add_argument("sent_flow_label")
args = parser.parse_args()

with open(file, "r") as my_file:
    data = my_file.read()
    
    # create list of returned flow-labels
    flow_labels = ["".join(x) for x in re.findall(pattern, data)]

    for index, item in enumerate(flow_labels):
        size = len(flow_labels[index])
        #print(a[index][:size - 37])
        flow_labels[index] = flow_labels[index][:size - 37]
        #print(f"Index:\t{index}")
        #print(a[index])

        # get the destination address, flow label tuple from the output
        #tuple = (a[index][151:158].replace(" ", ""), (a[index][24:72].replace(" ", "")).replace("\n", ""))

        ip = (flow_labels[index][24:72].replace(" ", "")).replace("\n", "")

        ipv6_addr = ipaddress.ip_address(int(ip, 16))
        #print(ipv6_addr)

        tuple = (str(ipv6_addr), flow_labels[index][151:158].replace(" ", ""))
        #print("Tuple:")
        #print(tuple)
        flow_label_list.append(tuple)
    
    # remove duplicate items from flow_label_list
    flow_label_list = list(dict.fromkeys(flow_label_list))

    #result = re.findall(IPV6ADDR, data)
    #print(result)

    #hop_list = my_file.read().splitlines() 
    hop_list = re.findall(IPV6ADDR, data) 

    # Remove first item in the list (the destination address) and add it as separate dictionary element
    dest = hop_list.pop(0)

    # Create top-level dictionary
    my_dict = {}
    #my_dict["probe_uuid"] = str(uuid.uuid4())
    #my_dict["flow_label"] = 100
    my_dict["outgoing_tcp_port"] = args.tcp_port
    my_dict["flow_label"] = args.sent_flow_label
    my_dict["timestamp"] = str(datetime.datetime.now())
    my_dict["source"] = args.source_ip
    my_dict["destination"] = dest

    count = 0 # in case items is empty and you need it after the loop
    #hop_dictionary = { index : item for index, item in enumerate(hop_list, start=1) }
    hop_dictionary = { index : {address : "x"} for index, address in enumerate(hop_list, start=1) }

#my_dict["hops"] = hop_dictionary

#json_file = args.file
#if json_file.endswith('.txt'):
    #json_file = json_file[:-4]

#json_file = json_file + ".json"

#path = f'/root/logs/{args.hostname}/' + os.path.basename(json_file)

#print(path)

#with open(path, 'w') as fp:
    #json.dump(my_dict, fp, indent=4)