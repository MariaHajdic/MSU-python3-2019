def root(ids, i):
    while i != ids[i]:
        i = ids[i]
    return i

def conn(ids, p, q):
    return root(ids, p) == root(ids, q)

def union(ids, sz, p, q):
    i = root(ids, p)
    j = root(ids, q)
    if i == j:
        return
    if sz[i] < sz[j]:
        ids[i] = j
        sz[j] += sz[i]
    else:
        ids[j] = i
        sz[i] += sz[j]

readyToStop = False
begin, end = "", ""
s = {}
k = 0
ids = []
sz = []
while True:
    a = input().split(" ")
    if len(a) == 1:
        readyToStop = True
        begin = a[0]
        break
    if not s.get(a[0], False):
        s[a[0]] = k
        ids.append(k)
        sz.append(1)
        k += 1
    if not s.get(a[1], False):
        s[a[1]] = k
        ids.append(k)
        sz.append(1)
        k += 1
    union(ids, sz, s[a[0]], s[a[1]])

end = input()

if (not s.get(begin, False)) or (not s.get(end, False)) or (not conn(ids, s[begin], s[end])):
    print("NO")
else:
    print("YES")
