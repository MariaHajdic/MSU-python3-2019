import math

def pigen():
    pi = 0
    i = 0
    while True:
        pi += 4.0 * ( (-1) ** (i % 2) ) / (2 * i + 1) 
        yield pi
        i += 1

exec(input())
exec(input())
