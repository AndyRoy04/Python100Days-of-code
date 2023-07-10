import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["build", "baboon", "camel", "shark", "banana"]
# lives = 6
chosen_word = random.choice(word_list) # random item choosen from list
print(f'see the guess : {chosen_word}')
lenght = len(chosen_word)
display = [] # innitializing an empty list to fill it with as many blanks as there are in the chosen_word
for letter in chosen_word: # replacing chosen_word() with blanks
    display += "-"
print(display)

choice = input("What difficulty do you want? (easy, medium, hard, extreme)").lower()
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

end_of_game = False
# while not end_of_game:
# string_display = ''

while not end_of_game:
    guess = input("Guess a letter : ").lower()  # prompting the user to guess a random letter
    

    for number in range(lenght):  # checking if the users letter is same with a char in the random choosen item
        letter = chosen_word[number]    
        if guess == letter:  # replacing list index with the users input if it matches a char in the random choosen item
            display[number] = guess
        
    print(' '.join(display))

    # chosen_word_list = chosen_word.split()
    if guess not in chosen_word:
        print(f"\n{guess} is not in the word")
        lives -= 1 
        print(stages[lives])
    
    if lives == 0 and "-" in display:
        print("Out of chances, You Lose 😢")
        end_of_game = True 

    # if "-" in display and lives == 0:
    #     print("You Lose 😢")
    #     end_of_game = True     
    if "-" not in display:
        print("Wow, You Won 🎉")
        end_of_game = True

print(f"The word is : {chosen_word}") # would join the elements together 
# using the empty string as a separator, resulting in the string
    # string_display = ''.join(map(str, display))
    # print("You win 🎉")


