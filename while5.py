# Counting the no.of digits in a given number.
# the technique of flat division is used.

count = 0
num = int(input('enter given number ;'))
while num > 0:
    num = num // 10
    count = count + 1
print(count)
