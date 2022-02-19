import logging, argparse, json, os

# Opens a log-file (.json) and checks if the flow-label has changed at any point 
# in the path to the destination.
# The result of the comparison, along with the filename, destination IP, TCP port-number
# and source flow-label is logged to a log-file.


default_dir = os.getcwd()

# initialize argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--directory", "-dir", "-d", const=default_dir, nargs='?', help="Directory containing json log files that you would like to run the flow-label check on")
parser.add_argument("--file", "-f", help="Json file that you would like to run the flow-label check on")
parser.add_argument("--log", "-l", const='/root/logs/flowlabel_compare.log', nargs='?', help="Specify a logfile. Default = /root/logs/flowlabel_compare.log")
#parser.add_argument('-v', '-V', '--v', '--V', action='store_true')  # verbose mode. currently not implemented
args = parser.parse_args()

# initialize logging:
logging.basicConfig(filename=args.log,
format='%(asctime)s %(levelname)-8s %(message)s',
level=logging.INFO,
datefmt='%Y-%m-%d %H:%M:%S')

if args.file:
    if os.path.isfile(args.file):
        print(args.file)
        with open(args.file, "r") as file:
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
    else:
        print(f"Error: '{args.file}' is not a file")
        exit(1)

if args.directory:
    try:
        for filename in os.listdir(args.directory):
            if (os.path.isfile(os.path.join(args.directory, filename))):
                with open(os.path.join(args.directory, filename), 'r') as file:
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
    except FileNotFoundError:
        print("Error: No such file or directory")
        exit(1)
    except NotADirectoryError:
        print("Error: Not a directory")
        print("Please use the --file option to compare single files. Use the -h argument for more info.")
        exit(1)
