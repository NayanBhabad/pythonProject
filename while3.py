# Program to find multiplication of ten numbers entered by user using while loop.

i = 1
multi = 1
while i <= 10:
    num = float(input('enter the number ;'))
    multi = multi * num
    i = i + 1
print(multi)
