from art import logo
print(logo)

while True:
  try:
    first_number = float(input("What is your first number? "))
  except ValueError:
    print("Enter a number.")
  else:
    break

print("+\n-\n*\n/")
operation = input("Pick an operation: ")

while True:
  try:
    second_number = float(input("What is the second number? "))
  except ValueError:
    print("Enter a number.")
  else:
    break