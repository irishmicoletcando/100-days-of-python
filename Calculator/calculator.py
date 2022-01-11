from art import logo

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

def calculator_program():
  second_trial = False
  print(logo)
  while True:
    try:
      first_number = float(input("What is your first number? "))
    except ValueError:
      print("Enter a number.")
    else:
      break

  while not second_trial:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")

    while True:
      try:
        second_number = float(input("What is the second number? "))
      except ValueError:
        print("Enter a number.")
      else:
        break

    calculator_operation(num1=first_number, num2=second_number, operation_inputted=operation)

    yes_or_no = input("Type 'y' to continue with the result, or type 'n' to exit. ").lower()
    if yes_or_no == "n":
      second_trial = True
      calculator_program()


calculator_program()

    