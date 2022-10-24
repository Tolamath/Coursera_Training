"""
This program checks if a year is a leap year
"""
def is_leap_year(year):
    """
    This function returns either true or false if a year is leap year or not
    """
    return (year % 4 == 0 and year % 100 !=0) or (year % 100 == 0 and year % 400 == 0)
print("Please enter a year number: ")
year_num = int(input())
print(is_leap_year(year_num))
