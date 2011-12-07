def calc_p(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def solve():
    n = 999999
    m = 0
    ans = [0] * 10
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ll = len(l)

    for i in range(ll):
        p = calc_p(ll - i - 1)
        a = n // p
        ans[i] = l[a]
        l.remove(l[a]);
        n -= a * p
    return "".join(map(str, ans))

print solve()
