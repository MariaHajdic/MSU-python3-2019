import math

inp = list(map(int,input().split(',')))
n, m = inp

num, power = len(str(n)), len(str(n * n))
line = "{:{a}} * {:<{a}} = {:<{b}}".format(1, 2, 3, a = num, b = power) # str
m_new = 1 + (m - len(line)) // (len(line) + 3)
cell = math.ceil(n / m_new)

print('=' * m)

for k in range(cell):
    for j in range(1, n + 1):
        lines = []
        for i in range(1, m_new + 1):
            if i + k * m_new <= n:
                lines.append( "{:{a}} * {:<{a}} = {:<{b}}".format(i + k * m_new, j, \
                    (i + k * m_new) * j, a = num, b = power) )
        print(" | ".join(lines))
    print("=" * m)   
