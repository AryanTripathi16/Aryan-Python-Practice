# Python script to print Pascal's Triangle.

def print_pascal_triangle(n):
  
    triangle = []

    for i in range(n):
       
        row = [1]
        if triangle:
           
            prev_row = triangle[-1]
           
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
           
            row.append(1)
        triangle.append(row)

    for i in range(n):
      
        print(" " * (n - i - 1), end="")
       
        for num in triangle[i]:
            print(num, end=" ")
        print()


num_rows = 5
print_pascal_triangle(num_rows)
