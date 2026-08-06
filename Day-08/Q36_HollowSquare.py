# print a Hollow Square pattern of asterisks

def print_hollow_square(size):
   
    for i in range(size):
       
        for j in range(size):
          
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        print()

square_size = 5

print_hollow_square(square_size)

