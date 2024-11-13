def palindrome_checker(num):
    numcopy = num
    reversed_num = 0
    
    while numcopy > 0:
        remainder = numcopy % 10
        reversed_num = reversed_num * 10 + remainder
        numcopy //= 10 

    if reversed_num == num:
        return True
    else:
        return False
    
print(palindrome_checker(121))  
print(palindrome_checker(123))  
