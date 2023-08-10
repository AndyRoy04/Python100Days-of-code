import random
from logo import logo, second_logo

def game_start(attempts):
    end_of_game = False
    while not end_of_game:
        guess = int(input("\nMake a guess: "))
        if attempts == 0:
            print(f"Sorry you are out of Guesses. The number is {random_guess}\n")
            end_of_game = True
        elif guess > random_guess:
            print("Higher than Number.\nGuess again.")
            print(f"You've {attempts} attempts remaining to guess the number.")
        elif guess < random_guess:
            print("Lower than Number.\nGuess again.")
            print(f"You've {attempts} attempts remaining to guess the number.")
        elif guess == random_guess:
            print(f"Correct guess 🎉. The number is {random_guess}\n")
            end_of_game = True  
        attempts -= 1      

guess_list = []
for i in range(1, 101):
    guess_list.append(i)
random_guess = random.choice(guess_list)
# print(random_guess) # Undo this to have a hint on the chosen number
print(second_logo)
print("Welcome to the Number Guessing Game.\n")
print("I am thinking of a number between 1 and 100.")
choice = input("Choose difficulty: Type 'easy' or 'hard' : ").lower()
if choice == 'easy':
    attempts = 10
    game_start(attempts)
else:
    attempts = 5
    game_start(attempts)

