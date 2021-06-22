# GCD of two numbers.
n1, n2 = input('enter two numbers').split()
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    dividend = n1
    divisor = n2
else:
    dividend = n2
    divisor = n1
while divisor != 0:
    rem = n1 % n2
    dividend = divisor
    divisor = rem
else:
    print("GCD of ", n1, "and", n2, "is = ", divisor)
