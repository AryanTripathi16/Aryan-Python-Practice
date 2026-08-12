# Question:Take a number from the user and print all list elements that are greater than that number.

def filter_greater_elements(numbers, threshold):
    return [x for x in numbers if x > threshold]

my_list = [5, 12, 3, 45, 7, 21, 14]

try:
    user_num = float(input("Enter a number: "))
    result = filter_greater_elements(my_list, user_num)
    print(result)
except ValueError:
    print("Please enter a valid numeric value.")
