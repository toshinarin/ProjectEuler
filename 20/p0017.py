c1 = [len("zero"), len("one"), len("two"), len("three"), len("four"), len("five"), len("six"), len("seven"), len("eight"), len("nine")]
c10 = [len("ten"), len("eleven"), len("twelve"), len("thirteen"), len("fourteen"), len("fifteen"), len("sixteen"), len("seventeen"), len("eighteen"), len("nineteen")]
c00 = [0, len("ten"), len("twenty"), len("thirty"), len("forty"), len("fifty"), len("sixty"), len("seventy"), len("eighty"), len("ninety")]
c000 = [len("hundred"), len("thousand")]

wc1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
wc10 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
wc00 = [0, "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
wc000 = ["hundred", "thousand"]

def getWordCount(n):
    if (n == 1000):
        return len("onethousand")
    nn = n
    cnt = 0
    word = ""
    hundreds = n / 100
    n = n - (hundreds * 100)
    if hundreds > 0:
        cnt += c1[hundreds]
        word += wc1[hundreds] + " "
        cnt += c000[0]
        word += wc000[0] + " "
    tens = n / 10
    n = n - (tens * 10)
    ones = n
    if tens > 1:
        cnt += c00[tens]
        word += wc00[tens] + " "
        if ones > 0:
            cnt += c1[ones]
            word += wc1[ones] + " "
    elif tens == 1:
        cnt += c10[ones]
        word += wc10[ones] + " "
    elif ones > 0:
        cnt += c1[ones]
        word += wc1[ones] + " "
    if hundreds > 0 and (tens > 0 or ones > 0):
        cnt += len("and")
        word += "and"
    print str(nn) + ": " + word
    return cnt

def solve():
    ans = 0
    for i in range(1, 1001):
        ans += getWordCount(i)
    return str(ans)

print "ans: " + solve()

