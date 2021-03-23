''' syntax ;
    for val in sequence :
        body of for '''
# range (start,stop,step-size).
# stop index will be excluded.
for x in range(1, 11, 2):
    print(x)

for x in range(0, 11, 2):
    print(x)

# val may be any variable.
y = [1, 2, 3, 5, 6]
sum = 0
for val in y:
    sum = sum + val
print(sum)

# printing no.s from one to ten using for loop.
for val in range(11):
    print(val)
