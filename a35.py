# To check the year is leap or not.

num = int(input("Enter any year ;"))
if num % 4 == 0 or num % 400 and num % 100 != 0:
    print(num, "is the leap year")
else:
    print(num, "is not a leap year")
