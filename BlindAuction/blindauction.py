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


blind_auction_program()