# Perfect number.
'''if the sum of perfect divisors(except itself) of any number are equal to that no.
then given no. is perfect..'''

num = int(input('enter number ;'))
sum = 0
for val in range(1, num):
    if num % val == 0:
        sum = sum + val
if sum == num:
    print('the no. is perfect.')

else:
    print('no. is not perfect.')
