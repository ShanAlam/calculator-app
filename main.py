from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operators = {
  "+" : add, 
  "-" : subtract,
  "*" : multiply, 
  "/" : divide
}

all_symbols = ""
for key in operators:
  all_symbols += key + " "

def calculator():
  
  print(logo)
  
  num1 = float(input("What's the first number? \n"))
  
  termination = False
  while termination == False:
    
    chosen_symbol = input(f"Pick an operation from the following: {all_symbols} \n")
    num2 = float(input("What's the next number? \n"))
    operator_function = operators[chosen_symbol]
    answer = operator_function(num1, num2)
    print(f"{num1} {chosen_symbol} {num2} = {answer}")
  
    is_done = input(f"Type 'y' to continue calculating with {answer}, otherwise type 'n' to start a new calculation").lower()
  
    if is_done == "y":
      num1 = answer
  
    elif is_done == "n":
      termination = True
      clear()
      calculator()
      
    else:
      print("Invalid input")


calculator()