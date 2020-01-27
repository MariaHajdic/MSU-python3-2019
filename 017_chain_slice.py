from itertools import chain, cycle, islice

def chainslice(a, b, *args):
    return islice(chain(*args), a, b)

exec(input())
