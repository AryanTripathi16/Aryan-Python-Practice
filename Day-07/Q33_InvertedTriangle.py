# Program to print an inverted right-angled triangle pattern of stars


height = 5

for i in range(height, 0, -1):
    
    for j in range(i):
        print("*", end=" ")
        
    print()
