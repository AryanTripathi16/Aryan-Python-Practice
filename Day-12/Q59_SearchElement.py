# Question:Take a list and an element from the user. Check whether that element exists in the list or not.

def check_element_exists():
    user_input = input("Enter list elements separated by spaces: ")
    numbers = user_input.split()

    target = input("Enter the element to search for: ")

    if target in numbers:
        print("Exists")
    else:
        print("Does not exist")


check_element_exists()
