def draw(area, squares):
    res = []
    for j in range(max(-area["up"]+area["down"], 1)):
        res.append([])
        for _ in range(max(-area["left"]+area["right"], 1)):
            res[j].append(".")

    for s in squares:
        for h in range(abs(s["h"])):
            stepY = h if s["h"] > 0 else -h-1
            for w in range(abs(s["w"])):
                stepX = w if s["w"] > 0 else -w-1
                res[s["y"]-area["up"]+stepY][s["x"]-area["left"]+stepX] = \
                    s["s"]
    return res

squares = []

while True:
    line = input().split(" ")
    stop = True
    for el in line:
        if el != "0":
            stop = False
            break
    if stop:
        break
    squares.append({
        "x": int(line[0]),
        "y": int(line[1]),
        "w": int(line[2]),
        "h": int(line[3]),
        "s": line[4],
    })

m = {
    "left": 0,
    "right": 0,
    "up": 0,
    "down": 0,
}
if squares[0]["w"] < 0:
    m["left"] = squares[0]["x"] + squares[0]["w"]
else:
    m["left"] = squares[0]["x"]

if squares[0]["h"] < 0:
    m["up"] = squares[0]["y"] + squares[0]["h"]
else:
    m["up"] = squares[0]["y"]

squares = [s for s in squares if s["w"] != 0 and s["h"] != 0]

for s in squares:
    bX = s["x"] + s["w"]
    bY = s["y"] + s["h"]
    if s["w"] < 0 and s["x"] > m["right"]:
        m["right"] = s["x"]
    if s["w"] > 0 and bX > m["right"]:
        m["right"] = bX
    if s["w"] < 0 and bX < m["left"]:
        m["left"] = bX
    if s["w"] > 0 and s["x"] < m["left"]:
        m["left"] = s["x"]
    if s["h"] > 0 and s["y"] < m["up"]:
        m["up"] = s["y"]
    if s["h"] < 0 and bY < m["up"]:
        m["up"] = bY
    if s["h"] < 0 and s["y"] > m["down"]:
        m["down"] = s["y"]
    if s["h"] > 0 and bY > m["down"]:
        m["down"] = bY

r = draw(m, squares)
for l in r:
    print("".join(l))
