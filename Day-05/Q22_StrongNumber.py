# 📝 Question:Write a Python program to check whether a number is a Strong Number or not.

import math

def is_strong_number(number):
   
    num_str = str(number)
    
    factorial_sum = sum(math.factorial(int(digit)) for digit in num_str)
    
    return factorial_sum == number

input_num = int(input("Enter a number: "))

if is_strong_number(input_num):
    print(f"{input_num} is a Strong Number.")
else:
    print(f"{input_num} is not a Strong Number.")
