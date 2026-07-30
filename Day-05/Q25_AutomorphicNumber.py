# 📝 Question:Write a Python program to check whether a number is an Automorphic Number or not.

def is_automorphic_number(number):
    
    square = number ** 2
    
    str_num = str(number)
    str_square = str(square)
    
    return str_square.endswith(str_num)

input_num = int(input("Enter a number: "))

if is_automorphic_number(input_num):
    print(f"{input_num} is an Automorphic Number.")
else:
    print(f"{input_num} is not an Automorphic Number.")
