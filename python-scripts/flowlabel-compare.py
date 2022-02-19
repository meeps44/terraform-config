import logging, argparse, json

# Opens a log-file (.json) and checks if the flow-label has changed at any point 
# in the path to the destination.
# The result of the comparison, along with the filename, destination IP and source flow-label
# is logged to a log-file.

# initialize logging:
logging.basicConfig(filename='/root/logs/comparison_output.log',
format='%(asctime)s %(levelname)-8s %(message)s',
level=logging.INFO,
datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser()
parser.add_argument("file1")
parser.add_argument('-v', '-V', '--v', '--V', action='store_true') 
# action='store_true' implies default=False. Conversely, you could have action='store_false', which implies default=True.
args = parser.parse_args()

with open(args.file1, "r") as file:
    data = json.load(file)
    print(data["hops"][1])
    source_flow_label = data['flow_label']

    for key, value in data['hops'].items():
        try:
            if (data['hops'][key]['returned_flow_label'] != source_flow_label):
                flow_label_changed = True
                break
            flow_label_changed = False
        except KeyError:
            print("KeyError")
            result = False
            break

