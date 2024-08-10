"""
    Linear Search Algorithm
    Name: Yuvan Krishnan K
    Date: 10-08-2024
"""

# Defining the function for linear search:

def lin_search_alg(list_A, target):
    """
        Searches for the value stored in the variable target,
        in the list provided as list1.
        1. list_A : Element to be searched (int)
    """
    flag=0
    for y in range(len(list_A)):
        # Checking if the element to be searched is present at the current index.
        if list_A[y] == target:
            flag=1
    return flag

# Defining the function to handle few edge cases.

def input_1(prompt):
    """
        To get valid input (Edge case handling)---
        1. prompt : The message to be displayed to the user.
        2. ValueError is an exception that occurs when a function 
           receives an argument of the correct type but an inappropriate value.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid Datatype, Enter an integer.")

# Get valid input for the number of elements in the list.
y = input_1("Enter the number of elements in the list: ")

# Number of elements cannot be negative.
if y < 0:
    print("Number of elements cannot be negative.")
else:
    list_A = []
    for y in range(1, y+1):
        # Get valid input for the elements in the list.
        y = input_1(f"Enter the elements {y}: ")
        list_A.append(y)
        # Get valid input for target value.
    target = input_1("Enter the target value : ")

    # Perform linear search on the list
    result = lin_search_alg(list_A, target)

    if result:
        print(f"Target fount at: {result}")
    else:
        # If the target element is not present in the list
        print("Target not found")