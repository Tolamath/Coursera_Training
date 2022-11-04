"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Name: Adisa Tolani Adekunle
"""
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:
        return (datetime.date(year+1, 1, 1) - datetime.date(year, month,1)).days
    return (datetime.date(year, month+1, 1) - datetime.date(year, month, 1)).days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1 <= month <= 12:
            if 1 <= day <= days_in_month(year, month):
                return True
    return False
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    date_difference = (datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        if date_difference > 0:
            return date_difference
    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    todays_year = (datetime.date.today()).year
    todays_month = (datetime.date.today()).month
    todays_day = (datetime.date.today()).day
    current_age = days_between(year, month, day, todays_year, todays_month, todays_day)
    return current_age
print(age_in_days(0, 1, 21))
