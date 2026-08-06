# Python script to print a Hollow Pyramid pattern of asterisks 

def print_hollow_pyramid(n):
  
    for i in range(n):
        
        print(" " * (n - i - 1), end="")
        
       
        for j in range(2 * i + 1):
           
            if j == 0 or j == 2 * i or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
                
       
        print()


pyramid_height = 5
print_hollow_pyramid(pyramid_height)
