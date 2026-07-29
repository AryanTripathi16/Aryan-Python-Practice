# Question:User se n lo aur Fibonacci series ke pehle n terms print karo.

n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci sequence up to {n} term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
      
        nth = a + b
        
        a = b
        b = nth
        count += 1
