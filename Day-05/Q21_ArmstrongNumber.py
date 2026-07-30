# 📝 Question:Write a Python program to check whether a number is an Armstrong Number or not.

def is_armstrong_number(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

input_num = int(input("Enter a number: "))

if is_armstrong_number(input_num):
    print(f"{input_num} is an Armstrong number.")
else:
    print(f"{input_num} is not an Armstrong number.")
