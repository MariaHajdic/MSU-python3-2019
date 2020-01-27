import random
width, height, solvable = map(int, input().split(","))


def neighbours(room):
    res = []
    if room[0] > 1:
        m = ((room[0] - 2, room[1]), (room[0] - 1, room[1]))
        res.append(m)
    if room[0] < height - 2:
        m = ((room[0] + 2, room[1]), (room[0] + 1, room[1]))
        res.append(m)
    if room[1] > 1:
        m = ((room[0], room[1] - 2), (room[0], room[1] - 1))
        res.append(m)
    if room[1] < width - 2:
        m = ((room[0], room[1] + 2), (room[0], room[1] + 1))
        res.append(m)
    return res


def createMaze(width, height, solvable):
    maze = [["#"]*width for i in range(height)]

    path = [(0, 0)]
    maze[0][0] = "."
    if not solvable:
        path.append((height - 1, width - 1))

    while path:
        room = path[-1]
        ns = list(
            filter(
                lambda m: maze[m[0][0]][m[0][1]] == "#",
                neighbours(room)
            )
        )
        if not ns:
            path.pop()
            continue
        new = random.choice(ns)
        path.append(new[0])
        maze[new[1][0]][new[1][1]] = "."
        maze[new[0][0]][new[0][1]] = "."
    return maze


for l in createMaze(width, height, solvable):
    print("".join(l))
