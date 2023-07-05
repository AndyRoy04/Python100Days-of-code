print("The rollercoster Game")
print('Welcome to the rollercoster')
height = int(input("Enter your height in cm : "))

if height >= 120:
    bill = 0
    print("You can ride here")
    age = int(input("Enter your age : "))
    if age>=45 and age<=55:
        bill = 0
        print("You're given a free ride")
    elif age > 18:
        bill = 12
        print("Adults pay $12")
    elif 12<age<18:
        bill = 7
        print("Youths pay $7")
    else:
        bill = 5
        print("Children pay $5")
    photos = input("Will like taking pictures ? y or n : ")
    if photos == 'y' :
        bill += 3
        print(f"You're bill will be ${bill}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("Go play somewhere else")