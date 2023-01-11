def is_year_leap(year):
    result = None
    if year >= 1582:
        if year % 4 != 0:
            result = False
        elif year % 100 != 0:
            result = True
        elif year % 400 != 0:
            result = False
        else:
            result = True
    return result

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_year_leap(year):
            return 29
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
"""
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
        """