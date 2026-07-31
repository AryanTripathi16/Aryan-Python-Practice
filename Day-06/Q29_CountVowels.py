# Question:Ek string me vowels (a, e, i, o, u) ki total count print karo.

user = input("Enter a word: ")
count = 0

for char in user:
    
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
       char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        count = count + 1

print("Total vowels:", count)