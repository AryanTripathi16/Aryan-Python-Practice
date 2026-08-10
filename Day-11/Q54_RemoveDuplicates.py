# Question:Write a Python program to remove duplicate elements from a list without changing the order of the remaining elements.


numbers = [1, 2, 2, 3, 4, 4, 1, 5]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)
