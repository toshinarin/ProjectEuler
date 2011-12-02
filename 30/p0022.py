import sys

def getSortedNameList():
    f =  open("names.txt", "r")
    str = f.readline()
    str = str.replace('"', '')
    l = str.split(',')
    l.sort()
    return l

def getStrScore(s):
    ans = 0
    b = ord('A') - 1
    for i in range(len(s)):
        ans += ord(s[i]) - b
    return ans

def solve():
    l = getSortedNameList()
    ans = 0
    for i in range(len(l)):
        ans += getStrScore(l[i]) * (i + 1)
    return ans

print str(solve())
    
