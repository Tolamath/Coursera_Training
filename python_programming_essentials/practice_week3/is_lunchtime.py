"""
This program checks if hour is lunctime
"""
def is_lunchtime_test(hour, is_am):
    """
    This function returns True if hour is 11am or 12pm
    False otherwise
    """
    if 1 <= hour <= 12:
        if hour == 11 and is_am is True:
            print(str(hour) + "AM"+" is lunchtime")
        elif hour == 12 and is_am is False:
            print(str(hour) + "PM"+" is lunchtime")
        elif is_am is True:
            print(str(hour) + "AM" + " is not lunchtime")
        else:
            print(str(hour) + "PM" + " is not lunchtime")
is_lunchtime_test(11, True)
is_lunchtime_test(12, True)
is_lunchtime_test(11, False)
is_lunchtime_test(12, False)
is_lunchtime_test(10, False)
