# BMI Calculator
weight = float(input("Enter Your weight in kg : "))
height = float(input("Enter your Height in m : "))
print("Your BMI is gotten from : weight/(height*height)")
BMI = weight / height**2
# net_BMI = int(BMI)
# print(BMI)
# new_BMI = str(net_BMI)
print(f"Your BMI is {BMI}kg/m2")
