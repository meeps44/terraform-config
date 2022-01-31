
with open("/Users/admin/Desktop/test-new.txt", "r") as my_file:
    # hop_list = my_file.readlines()
    hop_list = my_file.read().splitlines() 
    # print(hop_list)

count = 0 # in case items is empty and you need it after the loop
hop_dictionary = { count : item for count, item in enumerate(hop_list, start=1) }
# hop_dictionary = { hop : "hop" for hop in hop_list }
# fruit_dictionary = { fruit : "In stock" for fruit in fruits }
print(hop_dictionary)