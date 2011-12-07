ans = ""
num = 1000000
n = 0
def dfs(sl, l):
    global ans, num, n
    if ans:
        return
    if len(l) == 0:
        n += 1
        if n == num:
            ans = "".join(map(str, sl))
        return
    for i in range(len(l)):
        tl = l[i]
        nsl = sl[:]
        nsl.append(tl)
        nl = l[:]
        nl.remove(tl)
        dfs(nsl, nl)

def solve():
    global ans
    dfs([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    return ans

print solve()
