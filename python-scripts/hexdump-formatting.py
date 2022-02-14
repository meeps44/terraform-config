import re

#new_regex = r"((([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n)"
#regex_tmp = "(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+"
#regex = "(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+"

reg = r"((([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+([0-9a-fA-F]+))+"
pattern = re.compile(reg)

my_file = "/home/erlend/git/terraform-config/python-scripts/example-output/example-output-1.txt"
#my_file = "/Users/admin/Dropbox/Skole/example-output-1.txt"

flow_label_list = []

with open(my_file, "r") as file:
    data = file.read()
    a = ["".join(x) for x in re.findall(pattern, data)]
    # result = re.findall(pattern, data)

    #size = len(a[0])
    #print(a[0][:size - 37])
    #print(a[1][:size - 37])

    for index, item in enumerate(a):
        size = len(a[index])
        #print(a[index][:size - 37])
        a[index] = a[index][:size - 37]
        #print(f"Index:\t{index}")
        #print(a[index])

        # get the destination address, flow label tuple from the output
        tuple = (a[index][151:158].replace(" ", ""), (a[index][24:72].replace(" ", "")).replace("\n", ""))
        #print("Tuple:")
        #print(tuple)
        flow_label_list.append(tuple)

# remove duplicate items from flow_label_list
flow_label_list = list(dict.fromkeys(flow_label_list))
print(flow_label_list)