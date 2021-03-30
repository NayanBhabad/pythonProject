# Multiplication table of any number entered by user using while loop.

num = int(input('enter the number;'))
i = 1
while i <= 10:
    multi = num * i
    i = i + 1
    print(num, '*', i, '=', multi)
