import argparse, json

# takes two json-files as input and compares the hop-list

parser = argparse.ArgumentParser()
parser.add_argument("file1")
parser.add_argument("file2")
args = parser.parse_args()

with open(args.file1, "r") as file1, open(args.file2, "r") as file2:
    # returns JSON object as a dictionary
    data1 = json.load(file1)
    data2 = json.load(file2)
    
    result = data1['hops']['2'] == data2['hops']['2']

    for key, value in data1['hops'].items():
        # print(f"{key}:{value}")
        try:
            result = data1['hops'][key] == data2['hops'][key]
        except KeyError:
            result = False
            break
    
    print(result)
