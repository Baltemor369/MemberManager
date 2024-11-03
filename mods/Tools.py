import re
from const import *
from datetime import datetime

def format_date(date_str):
    # get a date DDMMYY
    match = re.match(REGEX_DATE_6, date_str)
    if match:
        day,month,year = match.groups()
        # Obtenir l'année actuelle
        current_year = datetime.now()
        first_two_digits = str(current_year)[:2]
        year = first_two_digits + year
        if valide_date(day,month,year):
            return f"{day}/{month}/{year}"
        else:
            return None

    # get a date DDMMYYYY
    match = re.match(REGEX_DATE_8, date_str)
    if match:
        day,month,year = match.groups()
        if valide_date(day,month,year):
            return f"{day}/{month}/{year}"
        else:
            return None
    
    return None

def valide_date(day:int, month:int, year:int):
    # verify date is a valid real date
    # check type of parameters
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        return False
    
    # check month
    if month < 1 or month > 12:
        return False
    # check day min max
    if day < 1 or day > 31:
        return False
    # check day for 30days month
    if month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    # check day for February
    if month == 2:
        # check leap year
        if year % 4 == 0 and (year % 100!= 0 or year % 400 == 0):
            return 1 <= day <= 29
        # classic year
        return 1 <= day <= 28
    return True

def clear_input(user_input:str):
    # remove special characters
    for elt in LIST_SUS_CHAR:
        user_input = user_input.replace(elt,"")
    clear_input = re.sub(REGEX_SANITIZED, "", user_input)
    return clear_input

# test format_date
# print(format_date("310121"))  # 31/01/2021
# print(format_date("31.01.21"))  # 31/01/2021
# print(format_date("31012020"))  # 31/01/2020
# print(format_date("31-01-2020"))  # 31/01/2020
# print(format_date("31012021A"))  # None
# print(format_date("31012021 01/01/2021"))  # None
# print(format_date("01/01/2021"))  # 01/01/2021