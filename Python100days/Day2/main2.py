# data types
# print("Anderson"[6])
# numb_1 = input("Enter a num : ")
# numb_2 = input("Enter another numb : ")

# print(18 + 8 + 2.6)
# num = 123
# print(type(num))  here is a type check

# char = input("Enter your name :")
# num_char = len(char)
# new = str(num_char)
# print("Your name has "+new+" characters")

# num = input("Enter a 2 digit number : ")
# numb_1 = int(num[0])
# numb_2 = int(num[1])
# result = numb_1 + numb_2
# print(result)

# print(3*3/3+3-3)

# BMI Calculator
# weight = input("Enter Your weight in kg : ")
# height = input("Enter your Height in m: ")
# print("Your BMI is gotten from : weight/(height*height)")
# new_weight = float(weight)
# new_height = float(height)**2
# BMI = new_weight / new_height
# net_BMI = int(BMI)
# new_BMI = str(net_BMI)
# print("Your BMI is : "+new_BMI+"kg/m2")

# print(round(5.76369/2, 3))

# score = 2
# score *= 3
# height = 1.83
# win = True
# print(f"Your score is {score}, you're height is {height}. all data is {win}")

# Life in weeks
# age = input("Enter your age : ")
# age_left = 90 - int(age)
# months = age_left * 12
# weeks = age_left * 52
# days = age_left * 365
# print(f"You have {days} days, {weeks} weeks and {months} months left.")

# Tip calculator
total_bill = float(input("Enter the total bill in FCFA : "))
tip = float(input("Enter the percentage tip you'll like to give : "))
people = int(input("Enter the number of People to split the bill to : "))
tip_bill = total_bill * (tip)/100
net_bill = total_bill + tip_bill
bill = net_bill / people
the_bill = round(bill, 2)
# the_bill = "{:.2f}".format(bill) #converting a float to 2dp string
print(f"Each person is to pay : {the_bill}")
