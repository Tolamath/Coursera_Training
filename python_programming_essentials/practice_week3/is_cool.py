"""
This program checks if name is either Joe, John or Stephen
"""
def is_cool(name):
    """
    This function returns True if either of the names being input matches
    and returns False if otherwise
    """
    list_of_names = ("Joe", "John", "Stephen")
    if name in list_of_names:
        return True
    return False
print(is_cool("Cat"))
