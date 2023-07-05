# We could also make use of the random.choice(list) fuction to get a random name easily
import random

print("Who will pay the bill?. Let's find out")
name_string = input("Enter everyone's name seperated by a comma : ")
name = name_string.split(", ") # Here we split and store the names in a list called names

length = len(name) # Here we get the number of items in the list

random_name = random.randint(0, length-1) # We then take a random number from 0 to the number of items

name_to_pay = name[random_name] # We then get the name a the random choosen index
# name_to_pay = random.choice(name) # Perfomes same funvtion as the line above. Its uses lesser lines of code

print(f"{name_to_pay} is going to buy the meal today!")