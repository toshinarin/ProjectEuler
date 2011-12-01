def getDivisorsSum(n):
    ans = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans += i
    return ans

def getDivisorsSumList(r):
    l = [0]
    for i in range(1, r + 1):
        l.append(getDivisorsSum(i))
    return l

def solve():
    aL = []
    l = getDivisorsSumList(10000)
    for a in range(10001):
        if a in aL:
            continue
        b = l[a]
        if b > 10000:
            continue
        if l[b] == a and a != b:
            aL.append(a)
            aL.append(b)
            print "a: " + str(a) + ", b: " + str(b)
    print aL
    ans = 0
    for i in range(len(aL)):
        ans += aL[i]
    return ans

print str(solve())
