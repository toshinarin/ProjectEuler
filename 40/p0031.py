pences = [1, 2, 5, 10, 20, 50, 100, 200]
lp = len(pences)
S = 200
n = 0

def dfs(m, s):
    global pences, S, n
    if s > S:
        return;
    if s == S:
        n += 1
        return
    for i in range(m, lp):
        dfs(i, s + pences[i])

def solve():
    dfs(0, 0)
    return str(n)

print solve()



     
    