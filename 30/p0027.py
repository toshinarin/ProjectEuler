import math

prime_numbers = []
not_prime_numbers = []
def is_prime(n):
    global prime_numbers, not_prime_numbers
    if n < 2:
        return False
    if n in prime_numbers:
        return True
    if n in not_prime_numbers:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            not_prime_numbers.append(n)
            return False
    prime_numbers.append(n)
    return True

def count_prime_numbers(a, b):
    ans = 0
    n = 0
    while is_prime(n * (n + a) + b) == True:
        #print "n: " + str(n) + " -> " + str(is_prime(n * (n + a) + b))
        ans += 1
        n += 1
    return ans

def solve(n):
    max_a = 0
    max_b = 0
    max_cnt = 0
    for a in range(-n + 1, n):
        for b in range(-n + 1, n):
            c = count_prime_numbers(a, b)
            if c > max_cnt:
                max_a = a
                max_b = b
                max_cnt = c
    print "a: " + str(max_a) + ", b: " + str(max_b) + ", count: " + str(max_cnt)
    return str(max_a * max_b)

print solve(1000)

def test():
    if count_prime_numbers(1, 41) != 40:
        return False
    if count_prime_numbers(-79, 1601) != 80:
        return False
    return True

#print "test result: " + str(test())

