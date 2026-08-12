# Question:Write a Python program to find the difference between the largest and smallest elements of a list.

def find_list_difference(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

my_list = [10, 3, 5, 6, 22, 1, 9]

print(find_list_difference(my_list))
