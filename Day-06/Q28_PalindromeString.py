# Question:Check karo ki diya gaya string palindrome hai ya nahi.

user_string = input("Enter a string: ")

reversed_string = user_string[::-1]

if user_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
