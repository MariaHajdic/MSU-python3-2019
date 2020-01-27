line = [list(x) for x in eval(input())]
intervals = []

for begin, end in sorted(line):
    if intervals and intervals[-1][1] >= begin :
        intervals[-1][1] = max(intervals[-1][1], end)
    else:
        intervals.append([begin, end])

res = 0
for x in intervals:
    res += x[1] - x[0]
print(res)
