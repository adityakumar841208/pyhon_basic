# 1. **Unique Elements in List**: Convert a list to a set to keep only unique elements.

my_list = [1, 2, 4, 5, 2, 5, 7, 8, 6, 5, 2, 3, 4, 5]

new_list= []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)


# print(list(set(my_list))) set do not preserve the postion



