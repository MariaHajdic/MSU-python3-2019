def condense(a, b, p, z):
    if b[0][0] == 0:
        for i in range(1, len(b)):
            if b[i][0] != 0:
                tmp = b[0]
                b[0] = b[i]
                b[i] = tmp
                z = z * (-1)
                break
    if b[0][0] == 0:
        return 0

    c = [[0 for i in range(len(b) - 1)] for j in range(len(b) - 1)]
    for i in range(len(b) - 1):
        for j in range(len(b) - 1):
            c[j][i] = b[0][0]*b[j+1][i+1] - b[0][i+1]*b[j+1][0]

    t = a[0][0]
    if len(c) == 1:
        return c[0][0] * z // (t**p)

    return condense(b, c, p - 1, z) // (t**p)


def det(m):
    z = 1
    if m[0][0] == 0:
        for i in range(1, len(m)):
            if m[i][0] != 0:
                a = m[0]
                m[0] = m[i]
                m[i] = a
                z = z * (-1)
                break
    if m[0][0] == 0:
        return 0

    b = [[0 for i in range(len(m) - 1)] for j in range(len(m) - 1)]
    for i in range(len(m) - 1):
        for j in range(len(m) - 1):
            b[j][i] = m[0][0]*m[j+1][i+1] - m[0][i+1]*m[j+1][0]
    return condense(m, b, len(m) - 2, z)


matrix = []
try:
    while True:
        matrix.append(list(map(int, input().split(","))))
except EOFError:
    print(det(matrix))
