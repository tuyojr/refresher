def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    leap = is_leap(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap:
        month_days[1] = 29
    day = month_days[month - 1]
    return day

year = int(input("Enter a year: "))
month = int(input("Enter a month number: "))
days = days_in_month(year, month)
print(days)