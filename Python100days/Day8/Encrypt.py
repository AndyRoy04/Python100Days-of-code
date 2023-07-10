def encrypt(plaintext, key):
    cipher_text = ''
    for i in plaintext:        
        position = alphabet.index(i)+key
        if position > len(alphabet)-1:
            position-=len(alphabet)
        cipher_text += alphabet[position]
    print(f"The encoded text is : {cipher_text}")
      
alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction = input("1: Encode\n2: Decode\nMake a choice : ")
text = input("Enter your message : ").lower()
shift = int(input("Enter your key number : "))
encrypt(plaintext=text, key=shift)
