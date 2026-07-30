# 📝 Question:Write a Python program to check whether a number is a Perfect Number or not.

def is_perfect_number(number):
    
    if number <= 0:
        return False
        
    divisor_sum = sum(i for i in range(1, (number // 2) + 1) if number % i == 0)
    
    return divisor_sum == number

input_num = int(input("Enter a number: "))

if is_perfect_number(input_num):
    print(f"{input_num} is a Perfect Number.")
else:
    print(f"{input_num} is not a Perfect Number.")
