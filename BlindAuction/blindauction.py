from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def blind_auction_program():
  name = input("What is your name? ")
  while True:
    try:
      bid_price = float(input("What's your bid? $"))
    except ValueError:
      print("Invalid. Please enter a number")
    else:
      break

  auction = {}
  auction["name"] = name
  auction["bidprice"] = bid_price
  print(auction)

def yes_or_no():
  ask_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if ask_bidder == "yes":
    clear()
    blind_auction_program()


blind_auction_program()
yes_or_no()