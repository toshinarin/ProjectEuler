def solve():
    a = 0
    b = 0
    c = 0
    for i in range(1000):
        for j in range(1000):
            if j < i:
                continue
            if 500000 + (i * j) - (1000 * i) - (1000 * j) == 0:
                a = i
                b = j
                c = 1000 - a - b
    print "a: " + str(a) + ", b: " + str(b) + ", c: " + str(c)
    return str(a * b * c)

print(solve())
