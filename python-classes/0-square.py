class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f'Square with size {self.__size}'

    def size(self):
        """
        Returns the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size




