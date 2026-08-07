# Question:Write a Python program to count the number of:

# Alphabets
# Digits
# Special Characters

def count_characters(text: str) -> tuple:
    alphabets = sum(1 for char in text if char.isalpha())
    digits = sum(1 for char in text if char.isdigit())
    special = sum(1 for char in text if not char.isalnum() and not char.isspace())
    return alphabets, digits, special

if __name__ == "__main__":
    sample_string = "Python_3.12 @ 2026!"
    alpha, dig, spec = count_characters(sample_string)
    print(f"Original String: {sample_string}")
    print(f"Alphabets: {alpha}")
    print(f"Digits: {dig}")
    print(f"Special Characters: {spec}")
