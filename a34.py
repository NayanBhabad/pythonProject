# Calculating DA as per rules.

a = int(input("enter salary :"))
if a >= 10000 and a <= 20000:
    print("DA is 10% of basic salary.")
elif a > 20000 and a <= 50000:
    print("DA is 15% of basic salary.")
elif a > 50000 and a <= 100000:
    print("DA is 20% of basic salary.")
elif a > 100000:
    print("DA is not given.")
