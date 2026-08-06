# Python script to print a Diamond Pattern of asterisks

def print_diamond(n):
   
    for i in range(n):
       
        print(" " * (n - i - 1), end="")
        
        print("* " * (i + 1))

   
    for i in range(n - 1):
       
        print(" " * (i + 1), end="")
       
        print("* " * (n - i - 1))


diamond_size = 5
print_diamond(diamond_size)
