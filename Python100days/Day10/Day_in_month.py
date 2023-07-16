print("\nWelcom to the days in month calculator")
def leap_year(year):
    new_year1 = year % 4
    new_year2 = year % 100
    new_year3 = year % 400
    if new_year1 == 0 and new_year2 != 0 or new_year3 == 0:
        print("\nThis is a Leap year")
        return True
    else:
        print("\nThis is not a Leap year")
        return False

def days_in_month(year, month):
    year = leap_year(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month"
        
    if month == 2 and year == True:
        month = month - 1
        month_days[1] = 29
        return month_days[month]
    else:
        month = month - 1
        return month_days[month]

year = int(input("Enter the year : "))
month = int(input("Enter the month number : "))
days = days_in_month(year, month)
print(f"There're {days} days in month {month}\n")