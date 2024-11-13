# 5. **Find Even and Odd Numbers**: Write a program that separates even and odd numbers from a list.


def findoddandeven(list):
    list1= []
    list2 = []
    for i in list:
        if i%2==0:
            list1.append(i)
        else:
            list2.append(i)
    return (list1,list2)

list1 = [4,3,5,6,8,4,54,3,45,2,35,42,354]
print(findoddandeven(list1))