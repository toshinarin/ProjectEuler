def add(a, b):
    a = str(a)
    b = str(b)
    la = len(a)
    lb = len(b)
    l = max(la, lb)
    ans = ""
    c = 0
    t = 0
    for i in range(l):
        n = 0
        m = 0
        if i < la:
            n = int(a[la - 1 - i])
        if i < lb:
            m = int(b[lb - 1 - i])
        t = n + m + c
        c = t / 10
        ans = str(t % 10) + ans
    if c > 0:
        ans = str(c) + ans
    return ans

def solve():
    nn = "0"
    n1 = "1"
    n2 = "1"
    ans = 2
    while len(nn) < 1000:
        nn = add(n1, n2)
        n1 = n2
        n2 = nn
        ans += 1
    return ans 

print str(solve())    