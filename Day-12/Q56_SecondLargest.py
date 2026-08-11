# Question:Write a Python program to find the second largest element in a list.

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float("-inf") else None


sample_list = [12, 35, 1, 10, 34, 1, 35]
result = find_second_largest(sample_list)

print(result)
