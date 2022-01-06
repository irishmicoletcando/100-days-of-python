from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

auction = {}
bidding_finished = False

def highest_bidder(auction_record):
  max_bid = 0
  winner_bid = ""
  for bid in auction_record:
    bid_amount = auction_record[bid]
    if bid_amount > max_bid:
      max_bid = bid_amount
      winner_bid = bid
  print(f"The winner is {winner_bid} with a bid of ${max_bid}.")

while not bidding_finished:
  name = input("What is your name? ").capitalize()
  while True:
    try:
      bid_price = float(input("What's your bid? $"))
    except ValueError:
      print("Invalid. Please enter a number")
    else:
      break
  
  auction[name] = bid_price
  ask_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if ask_bidder == "no":
    bidding_finished = True
    highest_bidder(auction)
  elif ask_bidder == "yes":
    clear()