import os  #We import the OS module so as to use the os.system(cls) funtion to wipe the screen after a bid has been made
from art import logo

Bidders_Dictionary = {}
answer = True
def register_bids(Records):
    highest = 0
    winner = ""
    for bidder in Records:
        amount = Records[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest}\n")

print("\nWelcome to the secret auction Bid Game.\n")
print(logo)
while answer:
    Bidders_name = input("Bidder enter your name : ").capitalize()
    Bidders_bid = int(input("Whats your Bid ? : $"))

    Bidders_Dictionary[Bidders_name] = Bidders_bid
    check = input("Are there other Bidders around ? Type 'Yes' or 'No'\n").lower()    
    if check == "yes":
        answer = True        
        os.system("cls")
    else:
        answer = False
        register_bids(Bidders_Dictionary)