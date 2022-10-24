"""
This program checks if number is even
"""
def is_even(num):
    """
    Takes in even num as a parameter and returns a boolean value
    (True/False) if it is even or not
    """
    if num % 2 == 0:
        print(True)
    else:
        print(False)
is_even(7)
