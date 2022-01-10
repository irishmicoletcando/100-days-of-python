from art import logo
print(logo)

def calculator_operation(num1, num2, operation_inputted):
  if operation_inputted == "+":
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
  elif operation_inputted == "-":
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")
  elif operation_inputted == "*":
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")
  elif operation_inputted == "/":
    answer = num1 / num2
    print(f"{num1} / {num2} = {answer}")

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