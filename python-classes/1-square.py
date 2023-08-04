"""ALX Task 1 of Python Classes and Objects"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(self, size=0):
            Constructor for the Square class.
            Args:
                size (int, optional): The size of the square. Defaults to 0.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Constructor for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


