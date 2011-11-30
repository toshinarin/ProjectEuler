maxIndex = 1000001
cntList = []
for i in range(maxIndex):
    cntList.append(-1)

def getChainCount(n):
    global maxIndex
    global cntList
    if (n == 0):
        return -1
    m = n
    cnt = 1
    while m != 1:
        if m < maxIndex and cntList[m] > 0:
            cnt += cntList[m] - 1
            break
        if m % 2 == 0:
            m = m / 2
        else:
            m = 3 * m + 1
        cnt += 1
    cntList[n] = cnt
    return cnt

def solve():
    maxCnt = 0
    n = 0
    for i in range(1, maxIndex):
        c = getChainCount(i)
        if (maxCnt < c):
            maxCnt = c
            index = i
    return "index: " + str(index) + ", cnt: " + str(maxCnt)

print "ans: " + solve()

    
