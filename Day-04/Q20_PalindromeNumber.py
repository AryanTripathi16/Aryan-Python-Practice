# Question:Check karo ki number palindrome hai ya nahi.

num = int(input("Enter a number: "))

temp = num
reverse_num = 0

while temp > 0:
    remainder = temp % 10
    reverse_num = (reverse_num * 10) + remainder
    temp = temp // 10

if num == reverse_num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
