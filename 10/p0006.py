def solve():
    maxNum = 100
    sSum = 0
    summ = 0
    sumS = 0
    for i in range(1, maxNum + 1):
        sSum += i * i
        summ += i
    sumS = summ * summ
    return str(sumS - sSum)

print(solve())
        
    
