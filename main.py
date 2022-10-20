from art import logo
from replit import clear


def add(n1, n2):
  return n1 + n2
  
def subtract(n1, n2):
  return n1 - n2
  
def multiply(n1, n2):
  return n1 * n2
  
def divide(n1, n2):
  return n1 / n2
  
def result(n1, n2):
  if operation == "+":
    return add(n1, n2)
  elif operation == "-":
    return subtract(n1, n2)
  elif operation == "*":
    return multiply(n1, n2)
  elif operation == "/":
    return divide(n1, n2)


end_of_program = False
while not end_of_program:
  print(logo)
  first_number = float(input("What's the first number?\n"))
  operation = input("+\n-\n*\n/\nPick an operation:\n")
  second_number = float(input("What's the next number?\n"))
  the_result = result(n1 = first_number, n2 = second_number)
  print(f"{first_number} {operation} {second_number} = {the_result}")

  again = True
  while again == True:
    go_again = input(f"Type 'y' to continue calculating with {the_result}, or type 'n' to start a new calculation:\n").lower()
    
    if go_again == 'y':
      operation = input("pick an operation:\n")
      next_number = float(input("What's the next number?\n"))
      prev_result = the_result
      the_result = result(n1 = prev_result, n2 = next_number)
      print(f"{prev_result} {operation} {next_number} = {the_result}")
      
    elif go_again == 'n':
      clear()
      again = False
      end = input("Do you want to exit the calculator?\nType 'y' or 'n':\n").lower()
      clear()
      if end == 'y':
        end_of_program = True
        print("Thanks for using our calculator :)")

    else:
      print("Invalid info!")
