import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
        'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcom to Andy's Password Generator!!")
number_letters = int(input("How many Letters do you want in your passowrd ? \n"))
number_numbers = int(input("How many Numbers do you want ?\n"))
number_symbols = int(input("How many Symbols do you want ?\n"))

rand_letters = ''
for new_letter in range(1, number_letters+1):
    rand_letters += random.choice(letters)
    
rand_numbers = ''
for new_number in range(1, number_numbers+1):
    rand_numbers += random.choice(numbers)

rand_symbols =''
for new_symbol in range(1, number_symbols+1):
    rand_symbols += random.choice(symbols)

password = rand_letters + rand_numbers + rand_symbols
print(f"Your password is : {password}") # Simple Password

# The random.sample() funct randomly select characters from the password string.
# The join() funct concatenates all the characters together into a single string.

new_password = ''.join(random.sample(password, len(password)))
print(f"Or do you prefere : {new_password}")   # Strong Password
