import operator

def checkhash(seq, f, mod):
    s1 = {}
    for i in seq:
        if s1.get(f(i) % mod, None) is None:
            s1[f(i) % mod] = 1
        else:
            s1[f(i) % mod] += 1
    mx = max(s1.items(), key=operator.itemgetter(1))[1]
    mn = min(s1.items(), key=operator.itemgetter(1))[1]
    return (mx, mn)

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

exec("\n".join(lines))
