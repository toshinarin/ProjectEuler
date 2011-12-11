def solve(w):
    if w < 3 or w % 2 == 0:
        return "can't solve."

    a = 2
    s = 1
    c = [1, 1, 1, 1]
    for i in range((w - 1) / 2):
        c[0] += a
        a += 2
        c[1] += a
        a += 2
        c[2] += a
        a += 2
        c[3] += a
        a += 2
        for j in range(4):
            s += c[j]
    return str(s)

print solve(1001)