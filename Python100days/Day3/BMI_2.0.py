weight = float(input("Enter Your weight in kg : "))
height = float(input("Enter your Height in m : "))
print("Your BMI is gotten from : weight/(height*height)")
BMI = round(weight / height**2, 2)
# net_BMI = int(BMI)
# print(BMI)
# new_BMI = str(net_BMI)
print(f"Your BMI is {BMI}kg/m2")
if BMI < 18.5 :
    print("You are Underweight")
elif 18.5 < BMI < 25 : 
    print("You've a Normal weight")
elif 25 < BMI < 30 :
    print("You are Overweight")
elif 30 < BMI < 35 :
    print("You are Obese")
else:
    print("You are Clinically Obese")