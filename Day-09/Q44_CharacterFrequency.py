# Question:Write a Python program to print the frequency of each character in a string.

from collections import Counter

def print_frequencies(text: str):
    frequencies = Counter(text)
    for char, count in frequencies.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    sample_string = "hello world"
    print(f"Original String: '{sample_string}'\nCharacter Frequencies:")
    print_frequencies(sample_string)
