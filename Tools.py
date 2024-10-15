import re
from const import *

def format_date(date_str):
    for pattern in [REGEX_DATE_1, REGEX_DATE_2]:
        match = re.match(pattern, date_str)
        if match:
            day, month, year = match.groups()
            year = year[-2:]
            return f"{day}/{month}/{year}"

    return None