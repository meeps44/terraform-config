import re

regex_tmp = "(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+"

reg = r"((([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+([0-9a-fA-F]+))"
new_regex = r"((([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n)"
pattern = re.compile(reg)

regex = "(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+\n(([0-9a-fA-F]+) )+"
my_file = "/Users/admin/Dropbox/Skole/example-output-1.txt"

with open(my_file, "r") as file:
    data = file.read()
    #result = re.search(pattern, data)
    result = re.findall(pattern, data)
    print(result[0])
    
    #x = re.findall(regex, data)
    #data.replace(" ", "")
    #print("Printing data")
    #print(x[0])

    #string_without_line_breaks = ""
    #for line in file:
        #stripped_line = line.rstrip()
        #string_without_line_breaks += stripped_line

    #print(string_without_line_breaks)