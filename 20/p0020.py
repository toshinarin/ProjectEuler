def solve():
    n = 1
    for i in range(2, 101):
        n *= i
    sN = str(n)
    ans = 0
    for j in range(len(sN)):
        ans += int(sN[j])
    return ans

print str(solve())
    
