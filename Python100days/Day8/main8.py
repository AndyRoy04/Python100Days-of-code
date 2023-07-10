
# def greet():
#     print("Hello Guys")
#     print("Today we're doing functions")
#     print("Let's do ceaSaer cipher")
# greet()

# function with name
# def say_hello(name):
#     print(f"Hello {name}")
#     print(f"Are you really my {name}")   
# say_hello("Besty") 

# function with multiple parameters
# def multiple(name, location):
#     print(f"Your name is {name} right !!!")
#     print(f"Hey {name}, how's {location} today?")
# multiple(location="Andy", name="Douala")

# Define a function called paint_calc() so that the code below works. 
# import math
# def paint_calc(height, width, cover):
#     num_of_cans = math.ceil((height*width)/cover)  #the ceil() func returns the smallest integer >= x.
#     print(f"You'll need {num_of_cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# def prime_check(number):
#     prime = True
#     if number == 2:
#         print(f"{number} is a prime number")
#     elif number%2==0:
#         print(f"{number} is not a prime number")
#     elif number%2==1:
#         for i in range(2, number):
#             if number%i==0:
#                 prime = False
#             # else:
#             #     prime = True
#         if prime:
#             print(f"{number} is a prime number")
#         else:
#             print(f"{number} is not a prime number")
# n = int(input("Check this number : "))
# prime_check(number=n)
    # list_text = ['.']*len(plaintext) # Filling an empty list with chars or strings
    # print(list_text)
    # list_text = []
    # list_text.append(position) # It adds many element at a time in a list

def caeser(entered_text, shift_key, shift_direction):
    if shift_direction == 1:  
        choosen_text = '' 
        for letter in entered_text:
            if letter in alphabet:
                position = alphabet.index(letter)+shift_key
                if position > len(alphabet)-1:
                    position%=len(alphabet)
                choosen_text += alphabet[position]
            else:
                choosen_text+=letter
        print(f"Your text is : {choosen_text}")
    elif shift_direction == 2:
        other_text = ''
        for letter in entered_text:
            if letter in alphabet:
                position = alphabet.index(letter)-shift_key
                if position < -1*(len(alphabet)-1):
                    absolute_position = abs(position)
                    position=absolute_position%len(alphabet)
                    position = -abs(position)
                other_text += alphabet[position]
            else:
                other_text+=letter 
        print(f"Your text is : {other_text}") 
    else:
        print("Invalid choice !!!")

    # for letter in entered_text:
    #     position = alphabet.index(letter)+shift_key        
    #     if shift_direction == 2:
    #         # shift_key *= -1  # This line encodes and decodes at thesame time since the 
    #         # Shift_key is multiplied by itself everytime the for loop runs  
    #         position = alphabet.index(letter)-shift_key
    #     elif position > len(alphabet)-1:
    #         position-=len(alphabet)
    #     choosen_text += alphabet[position]
    # print(f"Your text is : {choosen_text}")    

    # def encrypt(plaintext, key):
    #     cipher_text = ''
    #     for letter in plaintext:         
    #         position = alphabet.index(letter)+key
    #         if position > len(alphabet)-1:
    #             position-=len(alphabet)
    #         cipher_text += alphabet[position]
    #     print(f"The encoded text is : {cipher_text}")
    # def decrypt(cipher, key):
    #     plain_text=''
    #     for letter in plaintext:
    #         position = alphabet.index(letter)-key
    #         plain_text += alphabet[position] 
    #     print(f"The decoded text is : {plain_text}") 

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PPaaaaaaa  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ... aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PPaaaaaaa 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ... 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""       
print(logo) 
   
alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = True
while answer: 
    direction = int(input("\n  Choices\n1: Encode\n2: Decode\nMake a choice : "))
    text = input("Enter your message : ").lower()
    shift = int(input("Enter your key number : "))
    # shift%=len(alphabet)
    caeser(entered_text=text, shift_key=shift, shift_direction=direction)

    get_answer = input("Type 'yes' to start over, otherwise 'no' to end the cipher : \n")
    if get_answer == 'no':
        answer = False
        print("Goodbye 🤝")
# if direction == 1:
#     text = input("Enter your message : ").lower()
#     shift = int(input("Enter your key number : "))
#     encrypt(plaintext=text, key=shift)
# else:
#     text = input("Enter your message : ").lower()
#     shift = int(input("Enter your key number : "))
#     decrypt(cipher=text, key=shift)
