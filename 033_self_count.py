class WeAre:
    _count = 0

    def __init__(self):
        self.__class__._count += 1

    def getx(self):
        return self._count

    def setx(self, value):
        pass

    def __del__(self):
        self.__class__._count -= 1

    def delx(self):
        pass

    count = property(getx, setx, delx, "")
    