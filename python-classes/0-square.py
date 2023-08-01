class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square with the given size."""
        self.__size = size

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
