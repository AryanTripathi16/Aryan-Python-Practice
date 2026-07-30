# 📝 Question:Write a Python program to check whether a number is a Neon Number or not.

def is_neon_number(number):
    
    square = number ** 2
    
    digit_sum = sum(int(digit) for digit in str(square))
    
    return digit_sum == number

input_num = int(input("Enter a number: "))

if is_neon_number(input_num):
    print(f"{input_num} is a Neon Number.")
else:
    print(f"{input_num} is not a Neon Number.")
