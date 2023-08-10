import random
from logo import logo, vs
from os import system # Import system from OS to enable us wipe the screen after use
from Game_data import data

def account_format(account):
    """"This functions takes as input the various account so as to assign different personalities to hte accounts"""
    return f"{account['name']}, a {account['description']} from {account['country']}"

def compare(user_choice, a_follower, b_follower):
    """Takes as input the users choice and compares to see if it's correct or not"""
    global score
    if user_choice == 'a':
        if a_follower > b_follower:
            score += 1 
            system("cls")
            print(logo)
            print(f"You're right, your Current score is {score}")          
        else:
            system("cls")
            print(logo)
            print(f"Sorry you're wrong. Your Final score is {score}")
            return True
    elif user_choice == 'b':
        if a_follower < b_follower:
            score += 1
            system("cls")
            print(logo)
            print(f"You're right, your Current score is {score}")           
        else:
            system("cls")
            print(logo)
            print(f"Sorry you're wrong. Your Final score is {score}")
            return True
    else:
        system("cls")
        print(logo)
        print("Wrong input")
        print(f"Your have {score} point")
        return True
# Start of main function
print(logo)
game_over = False
score = 0
second_account = random.choice(data)
while not game_over:
    first_account = second_account
    second_account = random.choice(data)
    while first_account == second_account:
        second_account = random.choice(data)

    print(f"Compare A: {account_format(first_account)}")
    print(vs)
    print(f"Against B: {account_format(second_account)}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower = first_account['follower_count']
    b_follower = second_account['follower_count']
    to_compare = compare(user_input, a_follower, b_follower)
    if  to_compare == True:
        game_over = True
