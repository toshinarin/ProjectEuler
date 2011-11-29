goal = 500
l = []
length = 0

def getNumList(maxN):
    l = [1]
    for i in range(1, maxN):
        l.append(l[i - 1] + i + 1)
    return l

def getDivisorsCount(n):
    c = 2
    i = 2
    m = int(n / 2 + 1)
    k = 0
    while i < m:
        if n % i == 0:
            #print "divided: " + str(i)
            n = n / i
            k += 1
        else:
            if (k > 0):
                c *= (k + 1)
                k = 0
            i += 1
        if n <= i:
            break
    #print "n: " + str(n)
    #print "c: " + str(c)
    return c

def solve():
    global l, length, goal
    maxN = 100000
    l = getNumList(maxN)
    #print "getNumList finished: " + str(l)
    length = len(l)

    ans = 0
    for i in range(maxN):
        d = getDivisorsCount(l[i])
        print "d: " + str(d)
        if (d > 500):
            ans = l[i]
            break

    return str(ans)

print(solve())
