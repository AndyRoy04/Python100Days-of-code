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