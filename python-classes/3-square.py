"""ALX Python Classes and objects task 3"""


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

        size(self):
            Getter method to retrieve the size attribute value.

        size(self, value):
            Setter method to set the size attribute value.
            Args:
                value (int): The new value for the size attribute.
            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.

        area(self):
            Calculates the area of the square.
            Returns:
                int: The area of the square.
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
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute value.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute value.

        Args:
            value (int): The new value for the size attribute.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
