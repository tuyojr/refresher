from art import logo
import os

clear = lambda: os.system('clear')

print("W E L C O M E    T O.")
print(logo)
print("The secret auction program.")

bidders = {}

def highest_bidder(registered_bidders):
    bidder = ''
    highest_bid = 0

    for key in registered_bidders:
        current_bid = registered_bidders[key]
        if current_bid > highest_bid:
            highest_bid = current_bid
            bidder = key
        
    print(f"The winner is {bidder} with a bid of ${current_bid}.")

bidding = True

while bidding:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bidders[name] = bid_amount

    if other_bidders == 'yes':
        clear()
    elif other_bidders == 'no':
        bidding = False
        highest_bidder(bidders)