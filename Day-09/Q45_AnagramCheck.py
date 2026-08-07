# Question:Write a Python program to check whether two strings are Anagrams or not.

def is_anagram(str1: str, str2: str) -> bool:
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()
    return sorted(clean_str1) == sorted(clean_str2)

if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    
    if is_anagram(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams.")
    else:
        print(f"'{string1}' and '{string2}' are not anagrams.")
