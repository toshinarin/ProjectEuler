def getDivisorsSum(n):
    ans = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans += i
    return ans

def getAbundantNumbers(r):
    l = []
    for i in range(r + 1):
        if i < getDivisorsSum(i):
            l.append(i)
    return l

def getSumTable(r, l):
    ans = [0] * (r + 1)
    ll = len(l)
    for i in range(ll):
        m = l[i]
        for j in range(i, ll):
            s = m + l[j]
            if s > r:
                break
            ans[s] = 1
    return ans

def solve(r):
    l = getAbundantNumbers(r)
    sL = getSumTable(r, l)

    ans = 0
    for i in range(r):
        if sL[i] == 0:
           ans += i
    return ans

print "answer: " + str(solve(28123))
