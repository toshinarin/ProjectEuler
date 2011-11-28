x = 600851475143
i = 2
list = []

while True:
    while x % i == 0:
        x = x / i
        list.append(i)
    i += 1
    if i > x:
        break
for j in list:
    print(j)
print "last prime: " + str(list[len(list) - 1])


