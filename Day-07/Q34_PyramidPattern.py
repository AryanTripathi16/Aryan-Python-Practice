# Program to print a full pyramid pattern of stars

height = 5

for i in range(1, height + 1):
    
    for j in range(height - i):
        print(" ", end="")
        
    for k in range(i):
        print("*", end=" ")
        
    print()
