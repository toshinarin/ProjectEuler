import math
def getPrimeNumList(searchRange):
    table = []
    i = 0
    n = searchRange
    for i in range(n + 1):
        if i == 2 or i % 2 == 1:
            table.append(1)
        else:
            table.append(0)

    maxN = int(math.sqrt(n)) + 1
    i = 1
    while i < maxN:
        i += 2
        if table[i] == 0:
            continue
        j = i + i
        while j <= n:
            table[j] = 0
            j += i

    numbers = []
    for i in range(2, n):
        if table[i] == 1:
            numbers.append(i)
    return numbers

def solve():
    primes = getPrimeNumList(2000000)
    l = len(primes)
    sum = 0
    for i in range(l):
        sum += primes[i]
    return str(sum)

print(solve())
