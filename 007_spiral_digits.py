n, m = eval(input())
spiral = (min(m, n) + 1) // 2
res = [[0] * n for i in range(m)]
num = 0

for i in range(spiral):
    for j in range(i, n - i):
        res[i][j] = num % 10
        num += 1
    for k in range(i + 1, m - i):
        res[k][n - i - 1] = num % 10
        num += 1
    if i != m - 1 - i:
        for j in range(n - i - 2, i - 1, -1):
            res[m - i - 1][j] = num % 10
            num += 1
    if i != n - i -1:
        for k in range(m - i - 2, i, -1):
            res[k][i] = num % 10
            num += 1

for row in res:
    print(*row)
