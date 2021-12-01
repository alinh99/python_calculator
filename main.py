#Calculator
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
print(logo)
def calculator():
  flags = True
  num1 = int(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  while flags:
    #Here we select "+"
    operation_symbol = input("Pick an operation: ") 
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    conti_cal = input(f"Type 'y' to continue calcuating with {answer}, 'r' to restart, or type 'n' to exit the program: ")
    
    if conti_cal == "y":
      num1 = answer
    elif conti_cal == "r":
      flags = False
      calculator()
    elif conti_cal == 'n':
      flags = False
    else:
      print("Please input a valid choice.")
      conti_cal = input(f"Type 'y' to continue calcuating with {answer}, 'r' to restart, or type 'n' to exit the program: ")
    if conti_cal == "y":
      num1 = answer
    elif conti_cal == "r":
      flags = False
      calculator()
    elif conti_cal == 'n':
      flags = False
    
calculator()