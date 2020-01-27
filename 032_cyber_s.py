from itertools import cycle
from math import ceil
from fractions import Fraction

class sausage():
    def __init__(self, meat = "pork!", length = 12):
        self.meat = meat
        self.length = ( length if float(Fraction(length)).is_integer() else int(Fraction(length) * 12) )
        self.loafs = ceil(self.length / 12)
        self.rem = ( self.length % 12 if self.length % 12 else 12 )

    def _skin(self, start, end):
        sk = ""
        for i in range(self.loafs):
            e = ("|" if i + 1 == self.loafs and self.rem < 12 else end)
            k = int(self.rem if i + 1 == self.loafs else 12)
            sk += (start + "-" * k + e)
        return sk

    def __str__(self):
        if self.length <= 0 or self.meat == "|":
            print("/|")
            for _ in range(3): print("||")
            return "\\|"

        print(self._skin("/", "\\"))
        
        ccl = cycle(self.meat)
        ln = [next(ccl) for _ in range(12)]
        filling = ""
        for i in range(self.loafs):
            e = int(self.rem if i + 1 == self.loafs else 12) 
            filling += "|" + "".join(ln[:e]) + "|"
        for _ in range(3): print(filling)

        return self._skin("\\", "/")

    def __add__(self, other):
        return sausage(self.meat, self.length + other.length)

    def __sub__(self, other):
        return sausage(self.meat, self.length - other.length)

    def __mul__(self, other):
        return sausage(self.meat, self.length * other)

    def __rmul__(self, other):
        return sausage(self.meat, self.length * other)

    def __truediv__(self, other):
        return sausage(self.meat, self.length / other)

    def __bool__(self):
        return True if self.length > 0 else False
