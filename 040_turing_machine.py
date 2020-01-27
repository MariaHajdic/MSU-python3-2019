class Action:
    def __init__(self, s):
        p = s.split(",")
        self.write = p[0]
        self.move = p[1]
        self.change = p[2]

lines = []
states = {}
try:
    while True:
        lines.append(input().split())
except EOFError:
    alf = lines[0]
    for i in range(1, len(lines) - 1):
        for j, ch in enumerate(alf):
            if lines[i][0] not in states:
                states[lines[i][0]] = {}
            states[lines[i][0]][ch] = Action(lines[i][j + 1])

string = list(lines[-1][0])
cur_state = "0"
cur_pos = 0
it = 0

while cur_state != "!" and it < 100000:
    act = states[cur_state][string[cur_pos]]
    if act.write != "":
        string[cur_pos] = act.write
    if act.move == "R":
        cur_pos += 1
        if cur_pos == len(string):
            string.append("_")
    if act.move == "L":
        cur_pos -= 1
        if cur_pos == -1:
            string.insert(0, "_")
            cur_pos = 0
    if act.change != "":
        cur_state = act.change
    it += 1

if it < 100000:
    print("".join(filter(lambda ch: ch != "_", string)))
