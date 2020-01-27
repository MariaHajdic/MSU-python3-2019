import sys

def BinPow(a, n, func):
    b = a
    for _ in range(n-1):
        a = func(a,b)
    return a

for line in sys.stdin:
    exec(line)
