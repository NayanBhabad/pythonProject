# Factorial of a number.

num = int(input('enter the number : '))
if num > 0:
    for val in range(1, num + 1):
        if num % val == 0:
            print(val)

else:
    print('Factorial of number is not possible.')
