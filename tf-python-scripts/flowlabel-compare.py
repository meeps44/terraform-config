import logging, argparse, json, os

# Opens a log-file (.json) or a directory containing log files, and checks if 
# the flow-label has changed at any point in the path to the destination.
# The result of the comparison, along with the filename, destination IP, TCP port-number
# and source flow-label is logged to a log-file.

#TODO: Implement counter measuring how many times the flow-label changed over
# a number of files


default_dir = os.getcwd()

# initialize argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--directory", "-dir", "-d", const=default_dir, nargs='?', help="Directory containing json log files that you would like to run the flow-label check on")
parser.add_argument("--file", "-f", help="Json file that you would like to run the flow-label check on")
parser.add_argument("--log", "-l", const='/root/logs/flowlabel_compare.log', nargs='?', help="Specify a logfile. Default = /root/logs/flowlabel_compare.log")
parser.add_argument("--verbose", "-v", action="store_true")
args = parser.parse_args()

# initialize logging:
logging.basicConfig(filename='/root/logs/flowlabel_compare.log',
format='%(asctime)s %(levelname)-8s %(message)s',
level=logging.INFO,
datefmt='%Y-%m-%d %H:%M:%S')

# initialize logging:
#logging.basicConfig(filename=args.log,
#format='%(asctime)s %(levelname)-8s %(message)s',
#level=logging.INFO,
#datefmt='%Y-%m-%d %H:%M:%S')

if args.file:
    if os.path.isfile(args.file):
        with open(args.file, "r") as file:
            data = json.load(file)
            destination_ip = data['destination']
            source_flow_label = int(data['flow_label'])
            tcp_port = data['outgoing_tcp_port']
            flow_label_changed = False
            hop_list = [] 

            for key, value in data['hops'].items():
                try:
                    if (data['hops'][key]['returned_flow_label'] != source_flow_label):
                        flow_label_changed = True
                        hop_number = key
                        hop_ip = data['hops'][key]['ipv6_address'] 
                        hop_flow_label = data['hops'][key]['returned_flow_label'] 
                        hop_list.append((hop_number, hop_ip, hop_flow_label))

                except KeyError:
                    print("KeyError")
                    exit(1)

            if (flow_label_changed):
                for item in hop_list:
                    print(f"File: {args.file}: Change in flow-label detected at hop {item[0]}. Sent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
                    #print(f"File: {args.file}: The flow-label changed in transit. Sent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
                    #print(f"The flow-label was changed while traversing the path to destination {destination_ip}.")
                    if args.verbose:
                        logging.info(f"\Checked file {args.file}\n \
                        Comparison result:\n \
                        Destination IP: {destination_ip}\n \
                        Source Flow label: {source_flow_label}\n \
                        Outbound TCP port: {tcp_port}\n \
                        Change in flow-label detected at hop number: {item[0]}\n \
                        From hop-IP: {item[1]}\n \
                        New flow-label: {item[2]}\n \
                        The flow-label was changed while traversing the path to destination {destination_ip}.")
                    else:
                        logging.info(f"File: {args.file}: Change in flow-label detected at hop {item[0]}. Sent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
            else:
                print(f"File: {args.file}: The flow-label did not change in transit.")
                #print(f"File:\t{args.file}: The flow-label was not changed while traversing the path to destination {destination_ip}.")
                # logging.info(f"Checked file {args.file}. Comparison result: The flow label did not change") # short version
                logging.info(f"File: {args.file}: The flow-label did not change in transit.")
            
        print("Comparison completed. Results logged to: /root/logs/flowlabel_compare.log")
    else:
        print(f"Error: '{args.file}' is not a file")
        exit(1)


if args.directory:
    try:
        for file in os.listdir(args.directory):
            if (os.path.isfile(os.path.join(args.directory, file))):
                filename = str(file)
                with open(os.path.join(args.directory, file), 'r') as file:
                    data = json.load(file)
                    destination_ip = data['destination']
                    source_flow_label = int(data['flow_label'])
                    tcp_port = data['outgoing_tcp_port']
                    flow_label_changed = False
                    hop_list = [] 

                    for key, value in data['hops'].items():
                        try:
                            if (data['hops'][key]['returned_flow_label'] != source_flow_label):
                                flow_label_changed = True
                                hop_number = key
                                hop_ip = data['hops'][key]['ipv6_address'] 
                                hop_flow_label = data['hops'][key]['returned_flow_label'] 
                                hop_list.append((hop_number, hop_ip, hop_flow_label))

                        except KeyError:
                            print("KeyError")
                            exit(1)

                    if (flow_label_changed):
                        for item in hop_list:
                            #print(f"File:\t{filename}: The flow-label was changed while traversing the path to destination {destination_ip}. \nSent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
                            print(f"File: {filename}: Change in flow-label detected at hop {item[0]}. Sent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
                            #print(f"File: {filename}: The flow-label changed in transit. Sent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
                            if args.verbose:
                                logging.info(f"\Checked file {filename}\n \
                                Comparison result:\n \
                                Destination IP: {destination_ip}\n \
                                Source Flow label: {source_flow_label}\n \
                                Outbound TCP port: {tcp_port}\n \
                                Change in flow-label detected at hop number: {item[0]}\n \
                                From hop-IP: {item[1]}\n \
                                New flow-label: {item[2]}\n \
                                The flow-label was changed while traversing the path to destination {destination_ip}.")
                            else:
                                logging.info(f"File: {filename}: Change in flow-label detected at hop {item[0]}. Sent flow-label: {source_flow_label}. Returned flow-label: {item[2]}")
                    else:
                        print(f"File: {filename}: The flow-label did not change in transit.")
                        # print(f"File:\t{filename}: The flow-label was not changed while traversing the path to destination {destination_ip}.")
                        # logging.info(f"Checked file {args.file}. Comparison result: The flow label did not change") # short version
                        logging.info(f"File: {filename}: The flow-label did not change in transit.") 

        print("Comparison completed. Results logged to: /root/logs/flowlabel_compare.log")
    except FileNotFoundError:
        print("Error: No such file or directory")
        exit(1)
    except NotADirectoryError:
        print("Error: Not a directory")
        print("Please use the --file option to compare single files. Use the -h argument for more info.")
        exit(1)
