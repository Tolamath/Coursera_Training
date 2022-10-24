"""
This program computes the name and age of a person
"""
def name_and_age(name, age):
    """
    This funciton returns the name and age of person
    And returns an error message is age is less than zero and greater than 100
    """
    if 0 < age < 100:
        print(f"{name} is {age} years old")
    else:
        print("Error: Input is not a two-digit number")
print("Enter your name: ")
person_name = input()
print("Please enter your age: ")
person_age = int(input())
name_and_age(person_name,person_age)
