import random

print("Place the Treasure Game")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
random_choice = ['11','12','13','21','22','23','31','32','33']
print(f"{row1}\n{row2}\n{row3}")
computer_choice = random.choice(random_choice)
# print(computer_choice)

answer = 3
while answer!=0:
    print("Possible entries are 11,12,13,21,22,23,31,32,33")
    print(f"You can gues {answer} times")
    position = input("Where do you think the treasure(🚨) is? : ")

    column = int(computer_choice[0])-1
    row = int(computer_choice[1])-1
    map[row][column] = '🚨'

    if position == computer_choice:
        print(f"\n{row1}\n{row2}\n{row3}")
        print("\n  🎉 You found it\n")
        answer = 0
    else:
        print("\n😒 Oops\n")
        answer-=1
        if answer == 0:
            print(f"The treasure is at position {computer_choice}\n")
        

