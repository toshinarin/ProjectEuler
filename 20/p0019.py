d30 = [9, 4, 6, 11]
y = 1900
m = 1

def jumpToNextMonthDay(n):
    global y, m, days
    if m in d30:
        n += 30
    elif m == 2:
        if y % 400 == 0:
            n += 29
        elif y % 100 == 0:
            n += 28
        elif y % 4 == 0:
            n += 29
        else:
            n += 28
    else:
        n += 31
    m += 1
    if m > 12:
        m = 1
        y += 1
    return n

def solve():
    global y, m
    n = 1
    cnt = 0
    while y < 2001:
        if n % 7 == 0 and y > 1900:
            print "y: " + str(y) + ", m: " + str(m)
            cnt += 1
        n = jumpToNextMonthDay(n)
    return str(cnt)

print solve()
    

        
    
    
    
