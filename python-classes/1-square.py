"""ALX Task 1 of Python Classes and Objects"""
class Square:
    def __init__(self, size=0):
        """Initialize a square with the given size"""
        self.__size = size

    @property
    def dict_(self):
        """Getter for the dictionary representation of the square"""
        return {'_Square__size': self.__size}

