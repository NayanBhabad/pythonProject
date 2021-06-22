# Program to find multiplication of ten numbers entered by user using for loop.

multi = 1
for num in range(1, 11):
    num = float(input("enter the numbers ;"))
    multi = multi * num
print(multi)
