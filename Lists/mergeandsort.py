# 3. **Merge and Sort Two Lists**: Write a function to merge two lists and sort the result.


def merge_and_sort(list1,list2):
    return list(list1+list2)

list1 = [4,4,5,6,2,6,3]
list2 = [3,42,4,2,44,21,4,5]

print(merge_and_sort(list1,list2))