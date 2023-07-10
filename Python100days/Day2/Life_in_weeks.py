age = input("Enter your age : ")
age_left = 100 - int(age)
months = age_left * 12
weeks = age_left * 52
days = age_left * 365
print(f"You have {days} days, {weeks} weeks, {months} months and {age_left} years left.")