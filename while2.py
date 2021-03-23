# Reverse the number.
num = int(input('enter the integer no.;'))
rev_num = 0
while num > 0:
    remainder = num % 10
    rev_num = (rev_num * 10) + remainder
    num = num // 10
print("The reverse number is ", rev_num)
