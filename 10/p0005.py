def solve():
    maxNum = 20
    numList = []
    dividedNumList = []
    for i in range(1, maxNum + 1):
        numList.append(i)

    divided = False
    n = 2
    while True:
        divided = False
        for j in range(0, maxNum):
            if numList[j] % n == 0:
                numList[j] = numList[j] / n
                divided = True
        if divided == True:
            dividedNumList.append(n)
        else:
            n += 1
            if n > maxNum:
                break

    ans = 1
    print numList
    print dividedNumList

    for i in dividedNumList:
        ans *= i
    for i in numList:
        ans *= i
    return str(ans)

print(solve())
