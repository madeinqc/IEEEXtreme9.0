import math

d = int(input())

for _ in range(d):
    t, a, b, c = [int(x) for x in input().split()]

    l = [a, b, c]
    l.sort()
    if l[0] + l[1] < l[2]:
        l[2] = l[0] + l[1]

    print(min(t, math.floor((l[0]+l[1]+l[2])/2)))
