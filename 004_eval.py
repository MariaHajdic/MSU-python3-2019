from math import *

fn = input()
left, right = map(float, input().split(sep=","))

def findRoot(left, right):
    middle = (right + left) / 2
    x = middle
    val = eval(fn)
    if abs(val) < 0.000001:
        return middle

    x = right
    border = eval(fn)
    if val*border > 0:
        return findRoot(left, middle)

    return findRoot(middle, right)

print(findRoot(left, right))
