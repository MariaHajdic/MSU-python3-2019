class morse:
    def __init__(self, line = "", b = "."):
        self.line = line
        self.buf = b
        self.dah = "dah"
        self.dit = "dit"
        self.di = "di"
        self.end = "."

        if line != "":
            l = line.split(" ")
            if len(l) == 1:
                self.di = l[0][0]
                self.end = ""
                if len(l[0]) == 2:
                    self.dit = self.di
                    self.dah = l[0][1]
                else:
                    self.dit = l[0][1]
                    self.dah = l[0][2]
                if len(l[0]) > 3: self.end = l[0][3]
            elif len(l) == 2:
                self.di = l[0]
                self.dit = self.di
                self.dah = l[1]
            else:
                self.di = l[0]
                self.dit = l[1]
                self.dah = l[2]
            if len(l) > 3: self.end = l[3]

    def __invert__(self):
        return morse(self.line, ", " + self.buf)
    
    def __pos__(self):
        k = ("" if self.line and len(self.line.split(" ")) == 1 else " ")
        return morse(self.line, self.di + k + self.buf)
            
    def __neg__(self):
        k = ("" if self.line and len(self.line.split(" ")) == 1 else " ")
        return morse(self.line, self.dah + k + self.buf)

    def __str__(self):
        if self.line and len(self.line.split(" ")) == 1:
            self.buf = self.buf.replace(self.di + ",", self.dit)
            self.buf = self.buf.replace(self.dah + ",", self.dah)
            self.buf = self.buf[: -1]
            if self.buf[-1] == self.di:
                self.buf = self.buf[:-1] + self.dit + self.end
            else:
                self.buf += self.end
        else:
            self.buf = self.buf.replace(self.di + " ,", self.dit + ",")
            self.buf = self.buf.replace(self.dah + " ,", self.dah + ",")
            self.buf = self.buf.replace(self.di + " .", self.dit + self.end)
            self.buf = self.buf.replace(self.dah + " .", self.dah + self.end)
        return self.buf
