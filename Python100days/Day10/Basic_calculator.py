from os import system
from logo import logo
# Add
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

# Below we create a dictionary to store all math functions created above
operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
    "%":Modulo,
}
# Here the function is used to call itself everytime we want to use a new calculator
def calculation(): 
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
        another_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start afresh or any other letter to exit: ").lower()

        if another_calculation == 'y':
            num1 = answer
        elif another_calculation == 'n':            
            system("cls")
            calculation()
        else:
            again = False   
# Main function below
calculation()