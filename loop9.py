# Largest of all three numbers.

a,b,c = (input("enter three numbers ;")).split()
a = int(a)
b = int(b)
c = int(c)
if a>=b and a>=c :
    print(a,'is the largest ')
elif b>=c and b>=a :
    print(b,'is the largest')
else : print(c,'is largest')