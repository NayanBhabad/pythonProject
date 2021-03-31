# The sum of even and odd no.s within a range given by user.

sume = 0
sumo = 0
N = int(input('Enter the natural no. up to which we have to find sum :'))
# We have taken range N+1 because last index get excluded in for loop.

for val in range(N + 1):
    if val % 2 == 0:
        sume = sume + val
    elif val % 2 == 1:
        sumo = sumo + val
    else:
        print('nothing')
print("the sum of odd numbers is ", sumo)
print("the sum of even numbers is ", sume)
