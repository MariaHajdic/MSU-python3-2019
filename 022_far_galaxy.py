class Galaxy:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

def distance(g1, g2):
    return (g1.x - g2.x) ** 2 + (g1.y - g2.y) ** 2 + (g1.z - g2.z) ** 2

gs = []
while True:
    line = input()
    if line == ".":
        break
    xraw, yraw, zraw, name = line.split(" ")
    g = Galaxy(float(xraw), float(yraw), float(zraw), name)
    gs.append(g)

max_dist = 0
res = ("", "")
for i in range(len(gs) - 1):
    for j in range(i + 1, len(gs)):
        d = distance(gs[i], gs[j])
        if d > max_dist:
            max_dist = d
            res = (gs[i].name, gs[j].name)

data = [res[0], res[1]]
data.sort()
print(data[0], data[1])
