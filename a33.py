# Implement a simple calculator.
import math as m

a = float(input("Enter first no.:"))
b = float(input("Enter second no.:"))
operation = input("enter operator :")

if operation == "+":
      print(a + b)
elif operation == "-":
      print(a - b)
elif operation == "*":
      print(a * b)
elif operation == "/":
      print(a / b)
elif operation == "s":
      print(m.sin(a))
elif operation == "c":
      print(m.cos(a))
elif operation == "t":
      print(m.tan(a))
elif operation == "l":
      print(m.log(a, 10))
elif operation == "sqrt":
      print(m.sqrt(a))
else:
      print("no such operation.")
