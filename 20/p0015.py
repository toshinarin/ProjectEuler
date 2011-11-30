cnt = 0

# it takes too long time...
def solve(x, y):
    global cnt

    for i in range(2):
        if i == 1:
            nx = x + 1
            ny = y
        else:
            nx = x
            ny = y + 1
#        print "nx: " + str(nx) + ", ny: " + str(ny)
        if nx < 20 and ny < 20:
            solve(nx, ny)
        else:
            cnt += 1
    return str(cnt)

def getP(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def solve2(x, y):
    ans = getP(x + y) / (getP(x) * getP(y))
    return str(ans)

#print str(getP(3))
print solve2(20, 20)    
    
