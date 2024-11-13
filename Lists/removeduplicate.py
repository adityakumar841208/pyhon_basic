# 2. **Remove Duplicates**: Given a list of integers, remove all duplicates and return a list of unique values.


# def remove_duplicate(lst):
#     unique_values = []
#     for item in lst:
#         if item not in unique_values:
#             unique_values.append(item)
#     return unique_values


# lst = [4, 3, 5, 3, 2, 6, 7, 3, 5]
# print(remove_duplicate(lst))

# optimized approach 
def remove_duplicate(lst):
    return list(set(lst))

lst = [4, 3, 5, 3, 2, 6, 7, 3, 5]
print(remove_duplicate(lst))

