import random
from logo import logo
from os import system

def game_cards():
    """"Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    a_card = random.choice(cards)
    return a_card

def summation(cards):
    """The summation function basically helps calculate the sum of cards in a list given it the user list ot dealer list. 
    It also checks to see if there's a black jack in the game"""
    if sum(cards) == 21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(player_score, dealer_score, dealer_card, player_card):
    if dealer_score == player_score:
        return "\tYou Draw 🙊"
    elif dealer_score == 0:
        return "\tComputer holds a blackjack you Lose 😭"
    elif player_score == 0:
        return "\tYou've a blackjack you win 🎉"
    elif dealer_score > 21:
        return "\tDealer went over 21. You win 🎉"
    elif player_score > 21:
        return "\tYou went over 21. You Lose 😭"
    elif player_score > dealer_score:
        return "\tYou win 🎉"
    else:
        return "\tYou Lose 😭"

def game_starts():
    print(logo)
    black_jack = 21
    player_card = []
    dealer_card = []    
    game_over = False
    
    for n in range(2):
        player_card.append(game_cards())
        dealer_card.append(game_cards())
    
    while not game_over: 
        player_score = summation(player_card)
        dealer_score = summation(dealer_card)
        print(f"\tYour cards are: {player_card}\n\tYour score is: {player_score}")
        print(f"\tComputer's first card is: {dealer_card[0]}\n")

        if player_score>21 or dealer_score>21:
            game_over = True
        elif (dealer_card[0]+dealer_card[1])==21:
            dealer_score = 0
            game_over=True
        elif (player_card[0]+player_card[1])==21:
            player_score = 0
        else:
            another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if another_card == 'y':
                player_card.append(game_cards())
            else:
                game_over = True

    while dealer_score != black_jack and dealer_score < 17:
        dealer_card.append(game_cards())
        dealer_score = summation(dealer_card)   

    print(compare(player_score, dealer_score, player_card, dealer_card))
    print(f"\tThe computer has : {dealer_card} and their score is {dealer_score}")
    print(f"\tYou have : {player_card} and your score is {player_score}")

while input("\nEnter 'y' to start the Game or 'n' to end the game : ") == 'y':
    system('cls')
    game_starts()
