# 1. **Word Frequency Counter**: Write a function to count the frequency of each word in a given string and store it in a dictionary.


word = "hey this is aditya how are you guys this is ayush."
words = word.split(" ")
dict = {}

#to check the letter
# for i in word:
#     if i not in dict:
#         dict[i] =1
#     elif i in dict:
#         dict[i] = dict[i]+1

for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

print(dict)
