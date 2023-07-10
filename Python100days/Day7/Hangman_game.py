# For more code explanation, go to main7.py

import random
from Hangman_lib import word_list, logo, stages #Importing a varaible from a module
print(logo)

lives = 6
end_of_game = False
chosen_word = random.choice(word_list) # random item choosen from list
# print(f'see the guess : {chosen_word}')
lenght = len(chosen_word)

display = [] # innitializing an empty list to fill it with as many blanks as there are in the chosen_word
for letter in chosen_word: # replacing chosen_word() with blanks
    display += "-"

choice = input("What difficulty do you want? (easy, medium, hard, extreme)\n").lower()
if choice == 'easy':
    lives = 6
elif choice == 'medium':
    lives = 5
elif choice == 'hard':
    lives = 4
elif choice == 'extreme':
    lives = 3
else:
    lives = round(4.5)
print(f"You start with {lives} lives")
while not end_of_game:
    guess = input("Guess a letter : ").lower()  # prompting the user to guess a random letter
    if guess in display :
        print(f"You guessed {guess} before")
    for number in range(lenght):  # checking if the users letter is same with a char in the random choosen item
        letter = chosen_word[number]    
        if guess == letter:  # replacing list index with the users input if it matches a char in the random choosen item
            display[number] = guess
        
    print(' '.join(display))

    if guess not in chosen_word:
        print(f"\n{guess} is not in the word")
        lives -= 1 
        print(stages[lives])
        print(f"You've {lives} lives left")
    
    if lives == 0 and "-" in display:
        print("Out of chances, You Lose 😢")
        end_of_game = True

    if "-" not in display:
        print("Wow, You Won 🎉")
        end_of_game = True

print(f"The word is : {chosen_word}") # would join the elements together 
# using the empty string as a separator, resulting in the string
