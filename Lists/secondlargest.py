# 4. **Second Largest Element**: Find the second largest element in a list of numbers.

def second_largest_element(list):
    first = second = float('-inf')
    for i in list:
        if first < i:
            second = first
            first = i
        elif second <i and first >i:
            second = i
    return second if second != ('-inf') else None

list= [4,2,5,6,2,1,6,7,43]
print(second_largest_element(list))
