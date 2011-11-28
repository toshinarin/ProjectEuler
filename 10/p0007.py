import math

def eratosthenes(n):
    table = []
    i = 0
    for i in range(100):
        if i == 2 or i % 2 == 1:
            table.append(1)
        else:
            table.append(0)
    for i in range(3, int(math.sqrt(n)) + 1):
        if table[i] == 0:
            continue
        for j in range(i + 1, n):
            table[j] = 0
    return table[n]

def solve(goal, searchRange):
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

    if goal < len(numbers):
        return str(numbers[goal - 1])
    else:
        return "the goal is not in range."
    return

print(solve(10001, 200000))
