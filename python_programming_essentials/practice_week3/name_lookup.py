"""
This program output the last name of a user, given the first name
"""
def name_lookup(first_name):
    """
    This function iterates over list of names and returns the surname for each
    for each first and also returns error - not an instructor if none is found
    """
    list_of_names = {"Joe": "Warren", "Scott": "Rixner", "John": "Greiner", "Stephen":"Wong"}
    if first_name in list_of_names:
        return list_of_names[first_name]
    return "Error: Not an instructor"
print("Enter the first name")
initial_name = input()
print("The surname is", name_lookup(initial_name))
