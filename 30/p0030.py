def get_powers(n, m):
    sn = str(n)
    ans = 0
    for i in range(len(sn)):
        ans += int(sn[i]) ** m
    return ans

def get_max_powers(n, m):
    return (9 ** m) * n

def solve():
    N = 5
    l = []
    b = 10
    i = 2
    while True:
        if i == b:
            b *= 10
            if i > get_max_powers(len(str(i)), N):
                break
        if i == get_powers(i, N):
            l.append(i)
            #print str(i) + ": " + str(get_powers(i, N))
        i += 1
    ans = 0
    for j in range(len(l)):
        ans += l[j]
    return str(ans)

print solve()
        
        