# Question:Write a Python program to count how many even and odd numbers are present in a list.

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens, odds = count_even_odd(sample_list)

print("Even numbers count:", evens)
print("Odd numbers count:", odds)
