# 1. **FizzBuzz**: Write a program that prints numbers from 1 to 100 with special rules:
#    - For multiples of 3, print "Fizz."
#    - For multiples of 5, print "Buzz."
#    - For multiples of both 3 and 5, print "FizzBuzz."

for i in range(101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz.", end="")
    elif i % 3 == 0:
        print("Fizz.", end="")
    elif i % 5 == 0:
        print("Buzz", end="")
    print(i)
