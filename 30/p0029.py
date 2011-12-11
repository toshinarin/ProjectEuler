def count_terms(n):
    s = set([])
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            s.add(a ** b)
    #print s
    return len(s)

def test():
    if count_terms(5) != 15:
        print count_terms(5)
        return False
    return True

#print "test result: " + str(test())

def solve():
    return str(count_terms(100))

print solve()