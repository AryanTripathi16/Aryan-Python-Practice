# Question:Write a Python program to remove all spaces from a string.

def remove_spaces(text: str) -> str:
    return text.replace(" ", "")

if __name__ == "__main__":
    sample_string = " P y t h o n   P r o g r a m "
    result = remove_spaces(sample_string)
    print(f"Original: '{sample_string}'")
    print(f"Modified: '{result}'")
