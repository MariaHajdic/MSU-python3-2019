def turtle(coord, direction):
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    while True:
        cmd = yield coord
        if cmd == 'f':
            coord = [coord[i] + dirs[direction][i] for i in range(2)]
        elif cmd == 'l':
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
