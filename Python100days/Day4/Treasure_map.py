# 🚨 Don't change the code below 👇
print("Place the Treasure Game")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("Possible entries are 11,12,13,21,22,23,31,32,33")
position = input("Where do you want to put the treasure(🚨)? ")
# 🚨 Don't change the code above 👆

column = int(position[0])-1
row = int(position[1])-1

map[row][column] = '🚨'
# treasure_position = map[row][column]
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")