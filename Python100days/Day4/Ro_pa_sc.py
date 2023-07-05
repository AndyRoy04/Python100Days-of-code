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
inputs = [rock, paper, scissors]

print("\nThe Rock, Paper, Scissors Game\n")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : \n"))

print(inputs[choose])

random_input = random.randint(0, 2)

print("Computer choose : ")
print(inputs[random_input])

if choose == random_input: 
    print("\nA Draw")
elif choose == 2 and random_input == 0 or choose == 0 and random_input == 1 or choose == 1 and random_input == 2:
    print("\nYou Loose")
elif choose == 0 and random_input == 2 or choose == 1 and random_input == 0 or choose == 2 and random_input == 1:
    print("\nYou Win")
elif choose >2 and choose<0:
    print("Wrong Choice!!!")

# Same program as above but longer
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