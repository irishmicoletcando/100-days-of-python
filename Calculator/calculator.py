from art import logo
print(logo)

operations = {
  "+": add,
  "-": subtract,
  "*": multiply, 
  "/": divide,
}

while True:
  try:
    first_number = float(input("What is your first number? "))
  except ValueError:
    print("Enter a number.")
  else:
    break

for symbols in operations:
  print(symbols)
operation = input("Pick an operation: ")

while True:
  try:
    second_number = float(input("What is the second number? "))
  except ValueError:
    print("Enter a number.")
  else:
    break