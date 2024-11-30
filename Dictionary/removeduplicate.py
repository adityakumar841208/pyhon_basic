# 5. **Dictionary Inversion**: Given a dictionary, invert it so keys become values and values become keys.

my_dict = {"aditya": "34", "ayush": "31", "miku": "14", "aman": "24"}

new_dict = {}

for key, value in my_dict.items():
    new_dict[value] = key

print(new_dict)

