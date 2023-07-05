# The random function is just like a random module 
# e.g a page of python code
# Also, each module performs a specific task

# A List is a data structure used for storing data in python

# The Append function is used to add an item to a list
# The extend([]) function is used to add multiple items to a list

# The variable.split("") function seperates a given text based 
# on the specified seperation argument in the parantheses

# We can also nest 2 lists together e.g list=[list1, list2]

# import random
# import module
# random_float = random.random()
# print(module.City)
# choice = random.randint(0, 1)
# if choice == 1:
#     print("Heads")
# else:
#     print('Tails')
# City = ["Adamawa", 'Bafoussam', 'Bamenda', 'Bertoua', 'Buea', 
# 'Douala', 'Ebolowa', 'Garoua', 'Maroua', 'Yaounde']
# choice = random.randint(0, 9)
# print(City(choice))
# City.extend(['Andyland', 'royland', 'Androy'])
# print(City)

# name_string = input("Enter everyone's name seperated by a comma : ")
# name = name_string.split(", ")
# length = len(name)
# random_name = random.randint(0, length-1)
# name_to_pay = name[random_name]
# print(f"{name_to_pay} is going to buy the meal today!")

# # 🚨 Don't change the code below 👇

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# print("Possible entries are 11,12,13,21,22,23,31,32,33")
# position = input("Where do you want to put the treasure(🚨)? ")
# # 🚨 Don't change the code above 👆

# column = int(position[0])-1
# row = int(position[1])-1

# map[row][column] = '🚨'
# # treasure_position = map[row][column]
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("The Rock, Paper, Scissors Game")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))

inputs = [rock, paper, scissors]
random_input = random.randint(0, 2)

# Same Code as the next on Below this
# if choose == 0:
#     if random_input == 0:
#         print(inputs[0])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nA Draw")
#     elif random_input == 1:
#         print(inputs[0])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nYou Loose")
#     elif random_input == 2:
#         print(inputs[0])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nYou Win")

# elif choose == 1:    
#     if random_input == 0:
#         print(inputs[1])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nYou Win")
#     elif random_input == 1:
#         print(inputs[1])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nA Draw")
#     elif random_input == 2:
#         print(inputs[1])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nYou Loose")

# elif choose == 2:    
#     if random_input == 0:
#         print(inputs[2])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nYou Loose")
#     elif random_input == 1:
#         print(inputs[2])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nYou Win")
#     elif random_input == 2:
#         print(inputs[2])
#         print("Computer choose : ")
#         print(inputs[random_input])
#         print("\nA Draw")
# else:
#     print("Wrong Choice!!!")
# # print(inputs[random_input])

if choose == random_input:
    print(inputs[choose])
    print("Computer choose : ")
    print(inputs[random_input])
    print("\nA Draw")
elif choose == 2 and random_input == 0 or choose == 0 and random_input == 1 or choose == 1 and random_input == 2:
    print(inputs[choose])
    print("Computer choose : ")
    print(inputs[random_input])
    print("\nYou Loose")
elif choose == 0 and random_input == 2 or choose == 1 and random_input == 0 or choose == 2 and random_input == 1:
    print(inputs[choose])
    print("Computer choose : ")
    print(inputs[random_input])
    print("\nYou Win")
else:
    print("Wrong Choice!!!")
