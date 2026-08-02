# Program to print an inverted full pyramid pattern of stars

height = 5

for i in range(height, 0, -1):
    
    for j in range(height - i):
        print(" ", end="")
        
    for k in range(i):
        print("*", end=" ")
        
    print()
