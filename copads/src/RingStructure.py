class RingList:
    """
    The RingList is a class implementing a circular list. The ring have a 
    fixed size and when it is full and you append a new element, the first 
    one will be deleted. The class lets you access to the data like a python 
    list or like a string.

    Adapted from: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/435902 
    Original author: Flavio Catalani
    """
    def __init__(self, length):
        self.__data__ = []
        self.__full__ = 0
        self.__max__ = length
        self.__cur__ = 0

    def append(self, x):
        if self.__full__ == 1:
            for i in range (0, self.__cur__ - 1):
                self.__data__[i] = self.__data__[i + 1]
            self.__data__[self.__cur__ - 1] = x
        else:
            self.__data__.append(x)
            self.__cur__ += 1
            if self.__cur__ == self.__max__:
                self.__full__ = 1

    def get(self):
        return self.__data__

    def remove(self):
        if (self.__cur__ > 0):
            del self.__data__[self.__cur__ - 1]
            self.__cur__ -= 1

    def size(self):
        return self.__cur__

    def maxsize(self):
        return self.__max__

    def __str__(self):
        return ''.join(self.__data__) 
        
