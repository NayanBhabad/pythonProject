# Use of 'nested if'.

'''You can have if statements inside if statements.'''

x = 30
if x > 10:
    print('above 10')
    if x > 20:
        print('above 20')
        if x > 25:
            print('above 25')
    else:
        print('below 20')
