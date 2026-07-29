# Question:User se ek number lo aur uska factorial print karo.

num = int(input("Ek number enter karein: "))

factorial = 1

if num < 0:
    print("Sorry, negative numbers ka factorial nahi hota.")
elif num == 0:
    print("0 ka factorial 1 hota hai.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"{num} ka factorial {factorial} hai.")
