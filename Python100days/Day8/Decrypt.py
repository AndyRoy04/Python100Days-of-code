def decrypt(cipher, key):
    cipher_text=''
    for letter in plaintext:
        position = alphabet.index(letter)-key
        cipher_text += alphabet[position] 
    print(f"The decoded text is : {cipher_text}")        
        
alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction = input("1: Encode\n2: Decode\nMake a choice : ")
text = input("Enter your message : ").lower()
shift = int(input("Enter your key number : "))
decrypt(cipher=text, key=shift)