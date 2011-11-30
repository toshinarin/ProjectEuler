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
    n = "2"
    for i in range(1, 1000):
        n = add(n, n)
    print n
    l = len(n)
    ans = 0
    for j in range(l):
        ans += int(n[j])
    return str(ans)

print solve()
    
