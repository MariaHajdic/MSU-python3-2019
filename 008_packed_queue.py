queue = eval(input())
elements = []

for q in queue:
    if isinstance(q, tuple):
        elements += list(q)
        continue
    if len(elements) < q:
        break
    print(tuple(elements[:q]))
    elements = elements[q:]
