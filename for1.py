# Using for loop finding the sum of odd and even no.s
sume = 0
sumo = 0
for val in range(11):
    if val % 2 == 0:
        sume = sume + val
    elif val % 2 == 1:
        sumo = sumo + val

print(sume, sumo)
