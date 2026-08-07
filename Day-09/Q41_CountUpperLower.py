# Question:Write a Python program to count the number of uppercase and lowercase letters in a given string.

def count_case(text: str) -> tuple:
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count

if __name__ == "__main__":
    sample_string = "Hello World! 2026"
    uppercase, lowercase = count_case(sample_string)
    print(f"Original String: {sample_string}")
    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")
