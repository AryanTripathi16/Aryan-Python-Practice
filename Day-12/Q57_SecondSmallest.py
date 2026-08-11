# Question:Write a Python program to find the second smallest element in a list.

def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None

    smallest = float("inf")
    second_smallest = float("inf")

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest if second_smallest != float("inf") else None


sample_list = [5, 2, 8, 2, 1, 9]
result = find_second_smallest(sample_list)

print(result)
