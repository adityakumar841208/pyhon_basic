# 1. **Unpack a Tuple**: Given a tuple with multiple elements, unpack its values into variables.


tuple = (1,2,3)
# a,*b,c = tuple the b takes the whole number in the list excludig the first and the last

a,b,c = tuple

print(a,b,c)