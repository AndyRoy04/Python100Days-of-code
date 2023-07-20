import random

def game_cards(): # This funstion is used to pick a random card from the deck of cards below
    """"Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    a_card = random.choice(cards)
    return a_card

def summation(cards): # The summation function just returns the sum of cards in a deck of cards
    """The summation function basically helps calculate the sum of cards in a list given it the user list ot dealer list. 
    It also checks to see if there's a black jack in the game"""
    if sum(cards) == 21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards) > 21 and len(cards)==2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def show_card(): # This funtion just outputs the finally results after the game ends
    print(f"\tThe computer has : {dealer_card} and their score is {dealer_score}")
    print(f"\tYou have : {player_card} and your score is {player_score}")

def compare(player_score, dealer_score): # The compare function is used to verify who won the game
    if dealer_score > 21:
        return "\tDealer went over 21. You win 🎉"
    elif (dealer_card[0]+dealer_card[1])==black_jack:
        return "\tComputer holds a blackjack you Lose 😭"
    elif (player_card[0]+player_card[1])==black_jack:
        return "\tYou've a blackjack you win 🎉"
    elif player_score > 21:
        return "\tYou went over 21. You Lose 😭"
    elif dealer_score == player_score:
        return "\tYou Draw 🙊"
    elif player_score > dealer_score:
        return "\tYou win 🎉"
    else:
        return "\tYou Lose 😭"

player_score = 0
dealer_score = 0
# Below we save the dealer and player's cards saved in 2 seperate lists 
player_card = []
dealer_card = []

for n in range(2):
    player_card.append(game_cards())
    dealer_card.append(game_cards())

game_over = False
while not game_over: 
    player_score = summation(player_card)
    dealer_score = summation(dealer_card)
    # print(player_card)
    # print(player_score)
    print(f"\tYour cards are: {player_card}\n\tYour score is: {player_score}")
    print(f"\tComputer's first card is: {dealer_card[0]}")

    black_jack = 21
    if player_score>21 or dealer_score>21:
        game_over = True
    else:
        another_card = input("Type 'y' to get another card or type 'n' to pass: ")
        if (another_card == "y"):
            player_card.append(game_cards())
        else:
            game_over = True

# else:
while dealer_score != black_jack and dealer_score < 17:
    # if dealer_score < 17:
        # dealer_random = random.choice(cards)
        # dealer_score += dealer_random
    dealer_card.append(game_cards())
    dealer_score = summation(dealer_card) 
    # else: 
    #     game_over = True   
show_card()
print(compare(player_score, dealer_score))
# if dealer_score > 21:
#     print("You win")
#     show_card()
#     # print(f"The computer has : {dealer_card} and their score is {dealer_score}")
#     # print(f"You have : {player_card} and your score is {player_score}")

# if dealer_score == player_score:
#     print("You Draw")
#     show_card()
#     # print(f"The computer has : {dealer_card} and their score is {dealer_score}")
#     # print(f"You have : {player_card} and your score is {player_score}")

# print(cards)
