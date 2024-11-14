# 2. **Merge Dictionaries**: Merge two dictionaries, adding values of common keys.
# from collections import Counter

dict1 = {
    "aditya":35,
    "ayush":30,
    "miku":22
}

dict2 = {
    "ram":22,
    "ayush":65,
    "roshan":42,
    "aditya":35
}

merge = {}

for i in dict1:
    sum[i] = dict1[i]

for i in dict2:
    if i in sum:
        sum[i] += dict2[i]
    else:
        sum[i] = dict2[i]

 # or
# merge = dict(Counter(dict1)+Counter(dict2))

print(merge)


