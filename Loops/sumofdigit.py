# 4. **Sum of Digits**: Given an integer, calculate the sum of its digits


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
    
print(sum_of_digits(13))