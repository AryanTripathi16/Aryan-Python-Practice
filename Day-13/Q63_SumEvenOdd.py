# Question:Write a Python program to find the sum of all even elements and the sum of all odd elements in a list.

def sum_even_odd(numbers):
    even_sum = sum(x for x in numbers if x % 2 == 0)
    odd_sum = sum(x for x in numbers if x % 2 != 0)
    return even_sum, odd_sum

my_list = [1, 2, 3, 4, 5, 6]

evens, odds = sum_even_odd(my_list)
print(f"Even sum: {evens}, Odd sum: {odds}")
