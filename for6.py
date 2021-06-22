# Prime number.

num = int(input('enter '))
if num > 1:
    for val in range(2, num):
        if num % val == 0:
            print('not prime')
            break
        else:
            print('prime')
else:
    print('not prime')
