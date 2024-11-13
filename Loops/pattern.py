# 5. **Pattern Printing**: Write a program to print a pyramid pattern using nested loops.


def pyramid_pattern(num):
    for i in range(num+1):
        print(" "*(num-i),end="")
        print("*"*(i*2-1))
        

pyramid_pattern(3)