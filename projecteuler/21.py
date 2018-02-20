import math

def proper_divisors(n):
    divs = list()
    for i in range(math.floor(n/2),0,-1):
        if not (n%i):
            divs.append(i)
    return divs

def d(a):
    total = 0
    for i in proper_divisors(a):
        total = total + i
    return total

amicable_set = set()
for a in range(1, 10000):
    for i in amicable_set:
        if a == i:
            continue
    if (a == d(d(a))) and (a != d(a)):
        amicable_set.add(a)
        amicable_set.add(d(a))

total = 0
for i in amicable_set:
    total = total + i
print(total)
