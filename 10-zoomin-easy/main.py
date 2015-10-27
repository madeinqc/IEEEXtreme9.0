w = int(input())
h = int(input())
n = int(input())

charmap = {}

for i in range(n):
    c = input()

    temp = []

    for r in range(h):
        temp.append(('%'+str(w)+'s') % input())

    charmap[c] = temp

q = int(input())

for _ in range(q):
    s = input()

    out = [''] * h

    for c in s:
        temp = charmap[c]
        for i in range(len(temp)):
            out[i] += temp[i]

    for x in out:
        print(x)
