# 📝 Question:Write a Python program to check whether a person is eligible to vote.

name = input("Enter the name: ")
age = int(input("Enter the age: "))

if age >= 18:
    print(f"{name} is eligible to vote")
else :
    print(f"{name} is not eligible to vote")
