from math import floor, log10


def card(n, c=0, prev=None):
    l = floor(log10(n or 1)) + 1

    if l == prev:
        return c

    return card(l, c+1, n)

i = input()

while i != 'END':
    print(card(int(i)))
    i = input()
