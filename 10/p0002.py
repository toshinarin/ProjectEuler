first = 1
second = 2
sum = 0
if first % 2 == 0:
    sum += first
if second % 2 == 0:
    sum += second

n = 0
while True:
    if n > 4000000:
        break;
    n = first + second;
    first = second
    second = n
    if n % 2 == 0:
        sum += n
print(sum)

