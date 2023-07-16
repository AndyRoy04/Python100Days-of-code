# # function with outputs
# def names(f_name, l_name):
#     """Here we take as input the 1st name and last name and 
#     convert their first letters to capital letters using the tittle()"""
#     if f_name == "" or l_name=='':
#         print("No valid inputs")
#     fname = f_name.title()
#     lname = l_name.title()
#     return f"{fname} {lname}"

# # nnames = names('', "anderson DJEUTIO")
# print(names("dfvwrSVD", "csd fvzc sddc"))

# print("\nWelcom to the days in month calculator")
# def leap_year(year):
#     new_year1 = year % 4
#     new_year2 = year % 100
#     new_year3 = year % 400
#     if new_year1 == 0 and new_year2 != 0 or new_year3 == 0:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     year = leap_year(year)
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month > 12 or month < 1:
#         return "Invalid month"

#     if month == 2 and year == True:
#         month = month - 1
#         month_days[1] = 29
#         return month_days[month]
#     else:
#         month = month - 1
#         return month_days[month]

# year = int(input("Enter the year : "))
# month = int(input("Enter the month : "))
# days = days_in_month(year, month)
# print(f"\nThere're {days} days in month {month}\n")

# Add
import os

def add(number1, number2):
    return number1 + number2
# Subtract
def subtract(number1, number2):
    return number1 - number2
# Divide
def divide(number1, number2):
    return number1 / number2
# multiply
def multiply(number1, number2):
    return number1 * number2
# Modulo
def Modulo(number1, number2):
    return number1 % number2

logo = """
 _____________________
|  _________________  |
| | Pythonista      | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_______________0.| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# Below we create a dictionary to store all math functions created above
operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
    "%":Modulo,
}
def calculation(): # Here the function is used to call itself everytime we want to use a new calculator
    print(logo)
    again = True
    num1 = float(input("\nEnter the first number : "))
    for symbol in operations:
        print(symbol)

    while again:
        operation_symbol = input("Choose a mathematical operation: ")
        num2 = float(input("Enter the next number : "))
        operation_choice = operations[operation_symbol]
        answer = operation_choice(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        another_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start afresh: ").lower()

        if another_calculation == 'y':
            # again = True
            num1 = answer
            # operation_symbol = input("Choose another mathematical operation: ")
            # num3 = float(input("Enter the other number : "))
            # operation_choice = operations[operation_symbol]
            # second_answer = operation_choice(first_answer, num3)
            # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        else:
            again = False
            os.system("cls")
            calculation()            
            # print("\nGood Bye 👋🏿\n")
calculation()
