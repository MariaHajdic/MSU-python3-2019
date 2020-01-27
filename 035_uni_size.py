def sizer(K):
    @property
    def size(self):
        try:
            return self.__size
        except:
            try:
                return len(self)
            except:
                return int(self)

    @size.setter
    def size(self, value):
        self.__size = value

    K.size = size
    return K
