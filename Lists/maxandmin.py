# 1. **Find Max and Min in List**: Write a function to find the maximum and minimum numbers in a list.

def max_min(list):
    max = 0
    min = 100
    for i in list:
        if i>max:
            max = i 
        if i < min:
            min = i

    return max,min


list = [4,5,3,6,2,7,3]

print(max_min(list))

