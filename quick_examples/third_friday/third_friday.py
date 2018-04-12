from datetime import date

def third_friday(year, month):
    first_day = date(year, month, 1)
    weekday_of_first_day = first_day.weekday()
    if weekday_of_first_day < 5:  # monday-friday
        day = 19 - weekday_of_first_day
    else:  # saturday-sunday
        day = 26 - weekday_of_first_day
    return date(year, month, day)