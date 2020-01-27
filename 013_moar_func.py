import sys

def moar(a, b, n):
    af, bf = 0, 0
    for i in range(len(a)):
        if a[i] % n == 0: af += 1
    for i in range(len(b)):
        if b[i] % n == 0: bf += 1
    return True if af > bf else False
    
for line in sys.stdin:
    exec(line)
