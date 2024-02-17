import random
import os
from art import logo

clear = lambda: os.system('clear')

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

blackjack = 0

option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def deal(n=1):
    return random.choices(cards, k=n)

def card_score(list_of_cards: list):
    score = sum(list_of_cards)
    blackjack = 21
    if score == blackjack:
        return 0
    if 11 in list_of_cards:
        if score > blackjack:
            list_of_cards.append(1)
            list_of_cards.remove(11)
    return score

while option != 'n':
    clear()
    
    print(logo)

    user = deal(2)
    computer = deal(2)

    user_total = card_score(user)
    computer_total = card_score(computer)

    computer_status = f"\tComputer's first card: {computer[0]}"

    print(f'\tYour cards: {user}, current score: {user_total}')
    print(computer_status)

    if user_total == blackjack or computer_total == blackjack or user_total > 21:
        break
    elif user_total < 21:
        prompt = input("Type 'y' to get another card, type 'n' to pass: ")
        if prompt == 'n':
            break
        elif prompt == 'y':
            user.extend(deal())
            user_total = card_score(user)
            print(f'\tYour cards: {user}, current score: {user_total}')
            if user_total > 21:
                print("You went over. You lose 😭")

    break