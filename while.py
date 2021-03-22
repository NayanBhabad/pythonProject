# Sum of odd and even no.s using while loop.

i = 1
sume = 0
sumo = 0
while i <= 10:
    if i % 2 == 0:
        sume = sume + i
        i += 1
    elif i % 2 == 1:
        sumo = sumo + i
        i += 1
print(sume, sumo)

i = 1
sume = 0
sumo = 0
while i <= 100:
    if i % 2 == 0:
        sume = sume + i
        i = i + 1
    elif i % 2 == 1:
        sumo = sumo + i
        i = i + 1
else:
    print('sum of even no. =', sume)
    print('sum of odd no. =', sumo)
