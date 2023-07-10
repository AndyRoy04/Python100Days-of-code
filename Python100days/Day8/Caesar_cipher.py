# For more detail explanationtof code, visit the main8.py file

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

from library import logo, alphabet

print(logo) 
answer = True
while answer: 
    direction = int(input("\n  Choices\n1: Encode\n2: Decode\nMake a choice : "))
    text = input("Enter your message : ").lower()
    shift = int(input("Enter your key number : "))
    caeser(entered_text=text, shift_key=shift, shift_direction=direction)

    get_answer = input("Type 'yes' to start over, otherwise 'no' to end the cipher : \n")
    if get_answer == 'no':
        answer = False
        print("Goodbye 🤝")
