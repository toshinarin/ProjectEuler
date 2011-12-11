def get_recurring_length(n):
    n = int(n)
    dl = []
    rl = []
    a = 1
    d = 0
    r = 0
    started = False
    while True:
        d = a / n
        dl.append(d)
        r = a % n
        if r != 0:
            started = True
        if started:
            if r in rl:
                break
            rl.append(r)
        a = 10 * r
    i = rl.index(r)
    if i > 0:
        rl = rl[i:]
    lrl = len(rl)
    return lrl, "0." + "".join(map(str, dl[1:-lrl])) + "[" + "".join(map(str, dl[-lrl:]))+ "]"

def solve():
    ans = 0
    ans_str = ""
    lr = 0
    max_lr = 0
    for i in range(2, 1000):
        lr, s = get_recurring_length(i)
        if lr > max_lr:
            max_lr = lr
            ans = i
            ans_str = s
    print ans_str
    return str(ans)

def test():
    for i in range(2, 13):
        lr, s = get_recurring_length(i)
        print "length: " + str(lr) + ", ans: " + s

#test()
print solve()