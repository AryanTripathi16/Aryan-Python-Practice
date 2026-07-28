# Question:Take a number n from the user and print the sum of the first n natural numbers.

n = int(input("Enter a positive number (n): "))

total_sum = 0
for i in range (1, n + 1):
    total_sum += i
print(f"The sum of the first {n} natural numbers is: {total_sum}")
