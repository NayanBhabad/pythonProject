# Multiplication table of any number entered by user using for loop.
num = int(input("enter the number ;"))
for val in range(1, 11):
    multi = num * val
    print(num, '*', val, '=', num * val)
