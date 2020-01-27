i = 0
prevArgs = None
begin, end, step = 0, 1, 1
cc = 0

def randrange(*args):
    global begin, end, step, i, prevArgs
    if prevArgs is not None and args == prevArgs:
        i += step
        if step > 0:
            while i >= end:
                i = begin + (i - end)
        else:
            while i <= end:
                i = begin - (end - i)
        return i

    if len(args) > 1:
        begin, end = args[0], args[1]
    else:
        begin, end = 0, args[0]
    if len(args) > 2:
        step = args[2]
    if begin > end and step == 1:
        step = -1
    prevArgs = args

    i = begin

    return i

def randint(a, b):
    global cc
    if cc % 2 == 0:
        cc += 1
        return a
    cc += 1
    return b
