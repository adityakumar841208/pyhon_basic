# 3. **Dictionar.y Sorting**: Sort a dictionary by its values in ascending order.

my_dict = {
    "aditya":34,
    "ayush":31,
    "miku":14,
    "aman":24
}

# sort by keys
# sortdict = sorted(my_dict.items()) 

# sort by value
sortdict = dict(sorted(my_dict.items(),key=lambda item:item[1]))

print(sortdict)
