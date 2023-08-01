class Square:
    def __init__(self, size=0):
        """Initialize a square with the given size"""
        self.__size = size

    @property
    def dict_(self):
        """Getter for the dictionary representation of the square"""
        return {'_Square__size': self.__size}


mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_)

mysquare = Square(89)
print(type(mysquare))
print(mysquare.dict_)

mysquare = Square()
print(type(mysquare))
print(mysquare.dict_)

try:
    mysquare = Square("3")
    print(type(mysquare))
    print(mysquare.dict_)
except Exception as e:
    print(e)

try:
    mysquare = Square(3.14)
    print(type(mysquare))
    print(mysquare.dict_)
except Exception as e:
    print(e)

try:
    mysquare = Square(-89)
    print(type(mysquare))
    print(mysquare.dict_)
except Exception as e:
    print(e)
