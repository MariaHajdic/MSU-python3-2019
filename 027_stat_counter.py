def statcounter():
    stats = {}

    def counter(f):
        if f not in stats:
            stats[f] = 0

        def newf(*args, **kwargs):
            stats[f] += 1
            return f(*args, **kwargs)
        return newf

    f = yield stats
    while True:
        f = yield counter(f)

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

exec("\n".join(lines))
