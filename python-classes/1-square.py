class Square:
    def __init__(self, size=0):
        """Initialize a square with a given size"""
        self.size = size

    @property
    def size(self):
        """Getter for size attribute"""
        return self._size

    @size.setter
    def size(self, size):
        """Setter for size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def dict_(self):
        """Return a dictionary representation of the square"""
        return {'size': self.size}


# Create a square with size 3
mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_())

# Create a square with size 89
mysquare = Square(89)
print(type(mysquare))
print(mysquare.dict_())

# Create a square with default size (0)
mysquare = Square()
print(type(mysquare))
print(mysquare.dict_())

# Try to create a square with invalid size (string)
try:
    mysquare = Square("3")
    print(type(mysquare))
    print(mysquare.dict_())
except Exception as e:
    print(e)

# Try to create a square with invalid size (float)
try:
    mysquare = Square(3.14)
    print(type(mysquare))
    print(mysquare.dict_())
except Exception as e:
    print(e)

# Try to create a square with invalid size (negative integer)
try:
    mysquare = Square(-89)
    print(type(mysquare))
    print(mysquare.dict_())
except Exception as e:
    print(e)
