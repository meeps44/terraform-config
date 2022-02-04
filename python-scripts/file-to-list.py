import json, uuid, argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()

# "/Users/admin/Desktop/test-new.txt"

with open(args.filepath, "r") as my_file:
    hop_list = my_file.read().splitlines() 

# Remove first item in the list (the destination address) and add it as separate dictionary element
dest = hop_list.pop(0)
dest_dict = { "destination": dest}

# Create top-level dictionary
my_dict = {}
my_dict["probe_uuid"] = str(uuid.uuid4())
# my_dict["flow_label"] = 100
my_dict["destination"] = dest

count = 0 # in case items is empty and you need it after the loop
hop_dictionary = { count : item for count, item in enumerate(hop_list, start=1) }

my_dict["hops"] = hop_dictionary

json_file = args.filepath
if json_file.endswith('.txt'):
    json_file = json_file[:-4]

json_file = json_file + ".json"

with open(f'{json_file}', 'w') as fp:
    json.dump(my_dict, fp, indent=4)
