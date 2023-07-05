# print("The rollercoster Game")
# print('Welcome to the rollercoster')
# height = int(input("Enter your height in cm : "))
# # if height >= 170 and age >= 17:
# if height >= 120:
#     bill = 0
#     print("You can ride here")
#     age = int(input("Enter your age : "))
#     if age > 18:
#         bill = 12
#         print("Adults pay $12")
#     elif 12<age<18:
#         bill = 7
#         print("Youths pay $7")
#     else:
#         bill = 5
#         print("Children pay $5")
#     photos = input("Will like taking pictures ? y or n : ")
#     if photos == 'Y' :
#         bill += 3
#         print(f"You're bill will be ${bill}")
#     else:
#         print(f"Your total bill is ${bill}")
# else:
#     print("Go play somewhere else")

# print("The Modulo !!!")
# number = float(input("Enter a number : "))
# mode = number%2
# if mode == 0:
#     print('The number is even')
# elif mode == 1:
#     print("The number is odd")
# else:
#     print("Not an integer")

# BMI Calculator
# weight = float(input("Enter Your weight in kg : "))
# height = float(input("Enter your Height in m : "))
# print("Your BMI is gotten from : weight/(height*height)")
# BMI = round(weight / height**2, 2)
# # net_BMI = int(BMI)
# # print(BMI)
# # new_BMI = str(net_BMI)
# print(f"Your BMI is {BMI}kg/m2")
# if BMI < 18.5 :
#     print("You're Underweight")
# elif 18.5 < BMI < 25 : 
#     print("You've a Normal weight")
# elif 25 < BMI < 30 :
#     print("You are Overweight")
# elif 30 < BMI < 35 :
#     print("You are Obese")
# else:
#     print("You're Clinically Obese")

# year = int(input("What year do you want to check  : "))
# new_year1 = year % 4
# new_year2 = year % 100
# new_year3 = year % 400
# if new_year1 == 0:
#     if new_year2 == 0:
#         if new_year3 == 0:
#             print("It's a Leap year")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("It'a a Leap Year")
# else:
#     print("Not a Leap Year")
# # if new_year1 == 0 and new_year2 != 0 and new_year3 == 0:
# #     print("It's a Leap year")
# # else:
# #     print("Not a Leap Year")

# print("Welcome to Andy's Pizzas")
# size = input("What pizza size do you want? S, M or L : ")
# pepperoni = input("Do you want pepperoni? Y or N : ")
# cheese = input("Do you want cheese? Y or N : ")
# bill = 0
# # Small size pizza calculation
# if size == 's':
#     bill = 15
#     print("Small Pizza : $15")
#     if pepperoni == 'y':
#         bill += 2
#         print("Pepperoni for Small Pizza : +$2")
#     if cheese == 'y':
#         bill += 1
#         print("Extra cheese for Pizza : +$1")
#     print(f"Your final bill is : ${bill}")
# # Medium size pizza calculation
# elif size == 'm':
#     bill = 20
#     print("Medium Pizza : $20")
#     if pepperoni == 'y':
#         bill += 3
#         print("Pepperoni for Medium Pizza : +$3")
#     if cheese == 'y':
#         bill += 1
#         print("Extra cheese for Pizza : +$1")
#     print(f"Your final bill is : ${bill}")
# # Large size pizza calculation
# elif size == 'l':
#     bill = 25
#     print("Large Pizza : $25")
#     if pepperoni == 'y':
#         bill += 3
#         print("Pepperoni for Large Pizza : +$3")
#     if cheese == 'y':
#         bill += 1
#         print("Extra cheese for Pizza : +$1")
#     print(f"Your final bill is : ${bill}")

# else:
#     print("No such Pizza size exist here")

# size = input("What pizza size do you want? S, M or L : ")
# pepperoni = input("Do you want pepperoni? Y or N : ")
# cheese = input("Do you want cheese? Y or N : ")
# bill = 0

# if size =='s':
#     bill +=15
# if size =='m':
#     bill +=20
# if size =='l':
#     bill +=25

# if pepperoni == 'y':
#     if size == 's':
#         bill += 2
#     else:
#         bill += 3

# if cheese == 'y':
#     bill += 1

# print(f"Your bill is : ${bill}")

# # Love calculator
# print("Welcome to the Love Calculator!")
# name1 = input("Enter your name : ")
# name2 = input("Enter their name : ")
# name3 = name1 + name2
# lower_case_name = name3.lower()
# number_T = lower_case_name.count('t')
# # print(f"T occurs {number_T} times")
# number_R = lower_case_name.count('r')
# # print(f"R occurs {number_R} times")
# number_U = lower_case_name.count('u')
# # print(f"U occurs {number_U} times")
# number_E = lower_case_name.count('e')
# # print(f"E occurs {number_E} times")
# total1 = number_T + number_R + number_U + number_E
# # print(f"Total = {total1}\n")
# number_L = lower_case_name.count('l')
# # print(f"L occurs {number_L} times")
# number_O = lower_case_name.count('o')
# # print(f"O occurs {number_O} times")
# number_V = lower_case_name.count('v')
# # print(f"V occurs {number_V} times")
# number_E = lower_case_name.count('e')
# # print(f"E occurs {number_E} times")
# total2 = number_L + number_O + number_V + number_E
# # print(f"Total = {total2}\n")
# Love = int(str(total1)+str(total2))

# if Love < 10 or Love > 90:
#     print(f"Your score is {Love}%, you go together like coke and mentos.\n")
# elif 40 <= Love <= 50:
#     print(f"Your score is {Love}%, you are alright together.\n")
# else:
#     print(f"Your score is {Love}%\n")


# print('''
#   ____________________________________________________________________
#  / \-----     ---------  -----------     -------------- ------    ---->
#  \_/__________________________________________________________________/
#  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
#  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
#  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
#  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
#  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
#  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
#  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
#  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
#  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
#  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
#  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
#  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
#  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
#  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
#  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
#  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
#  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
#  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
#  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
#  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
#  / \----- ----- ------------  ------- ----- -------  --------  -----/ >
#  \_/________________________________________________________________\_/

# ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("You're at a cross road. Where do you want to go? 'Left' or 'Right'\n")



if left_right == 'left' or left_right == 'Left' or left_right == 'LEFT':
    swim_wait = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if swim_wait == 'wait':
        doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if doors == 'yellow':
            print('You found the treasure! You Win!')
        elif doors == 'blue':
            print('You enter a room of beasts. Game Over.')
        elif doors == 'red':
            print("It's a room full of fire. Game Over")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print('You get attacked by an angry trout. Game Over.')
else:
    print('You fell into a hole. Game Over.')