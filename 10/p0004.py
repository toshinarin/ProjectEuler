def isPalindromic(strr):
    l = len(strr)
    c = l / 2
    for i in range(c):
        if strr[i] != strr[l - i - 1]:
            return False
    return True

def solve():
    list = []
    for i in range(900):
        for j in range(900):
            if isPalindromic(str((999 - i) * (999 - j))):
                list.append((999 - i) * (999 - j))
    list.sort()
    return str(list[len(list) - 1])

print solve()
    
    

