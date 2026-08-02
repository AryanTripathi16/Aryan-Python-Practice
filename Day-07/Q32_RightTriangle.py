# Program to print a right-angled triangle pattern of stars

height = 5

for i in range(1, height + 1):
   
    for j in range(i):
        print("*", end=" ")
        
    print()