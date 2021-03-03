a = input("enter first side ;")
b = input("enter second side ;")
c = input("enter third side ;")
a = int(a)
b = int(b)
c = int(c)
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(area)
