idxs = set({})
count = 0

input()
while True:
    line = list(input())
    if line[0] == '-':
        count += len(idxs)
        break

    prev_idxs = idxs.copy()
    idxs.clear()
    rect = False
    start = 0

    for i, l in enumerate(line):
        if l == '#' and not rect:
            rect = True
            start = i
        elif rect and l != '#':
            rect = False
            idxs.add((start, i - 1))

    count += len(prev_idxs - idxs)

print(count)
