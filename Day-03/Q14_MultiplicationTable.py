# Question:Take a number from the user and print its multiplication table up to 10.

num = int(input("Enter a number: "))

for i in range (1 , 11):
    print (f"{num} X {i} = {num * i}")