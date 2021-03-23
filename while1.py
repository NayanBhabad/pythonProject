# Sum of natural numbers.

'''sum = 0
i = 1
N = int(input("enter the natural no. up to which we have to find sum;"))
while i<=N :
    sum = sum + i
    i = i+1
print('The sum of natural no. is ',sum )'''

# Sum of even and odd natural numbers.

i = 1
N = int(input('enter natural no.'))
sume = 0
sumo = 0
while i <= N:
    if i % 2 == 0:
        sume = sume + i
        i = i + 1
    elif i % 2 == 1:
        sumo = sumo + i
        i = i + 1
print(sume, sumo)
