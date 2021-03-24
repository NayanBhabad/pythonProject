# Largest among three numbers.

a, b, c = input("Enter three numbers :").split()
a = float(a)
b = float(b)
c = float(c)

if a > b and a > c:
    print(a, ' is largest')
elif b > a and b > c:
    print(b, ' is largest')
else:
    print(c, 'is largest')
