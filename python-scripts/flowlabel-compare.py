import logging, argparse, json

# Opens a log-file (.json) and checks if the flow-label has changed at any point 
# in the path to the destination.
# The result of the comparison, along with the filename, destination IP, TCP port-number
# and source flow-label is logged to a log-file.

# initialize logging:
logging.basicConfig(filename='/root/logs/comparison_output.log',
format='%(asctime)s %(levelname)-8s %(message)s',
level=logging.INFO,
datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser()
parser.add_argument("file1")
#parser.add_argument('-v', '-V', '--v', '--V', action='store_true')  # verbose mode. currently not implemented
args = parser.parse_args()

with open(args.file1, "r") as file:
    data = json.load(file)
    print(data["hops"][1])
    destination_ip = data['destination']
    source_flow_label = int(data['flow_label'])
    tcp_port = data['outgoing_tcp_port']

    for key, value in data['hops'].items():
        try:
            if (data['hops'][key]['returned_flow_label'] != source_flow_label):
                flow_label_changed = True
                hop_number = key
                hop_ip = data['hops'][key]['ipv6_address'] 
                logging.info(f"\Checked file {args.file}\n \
                Comparison result:\n \
                Destination IP: {destination_ip}\n \
                Source Flow label: {source_flow_label}\n \
                Outbound TCP port: {tcp_port}\n \
                Change in flow-label detected at hop number: {hop_number}\n \
                with hop-IP: {hop_ip}\n \
                The flow-label was changed while traversing the path to destination {destination_ip}.")
                print(f"The flow-label was changed while traversing the path to destination {destination_ip}.")
            else:
                flow_label_changed = False
                logging.info(f"\nChecked file {args.file}\n \
                Comparison result: The flow-label was not changed while traversing the path to destination {destination_ip}.")
                print(f"The flow-label was not changed while traversing the path to destination {destination_ip}.")
        except KeyError:
            print("KeyError")
            exit(1)