import sys
from functools import reduce
from math import floor, log10, factorial
import operator

def countdigit(n):
    return floor(log10(n or 1)) + 1

n = 2
c = [None, 1]

num = 4
denum = 2

while countdigit(c[-1]) <= 308:
    c.append(num // denum)
    num //= n + 2
    num *= reduce(operator.mul, range(2 * n + 1, (n + 1) * 2 + 1))
    n += 1
    denum *= n

count = 0

for line in sys.stdin:
    if count < 100:
        i = int(line)
        print(c.index(i)+2)
