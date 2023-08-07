"""ALX Task 9"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square with a side length, x-coordinate, y-coordinate, and unique ID.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object with the given side length, x-coordinate, y-coordinate, and ID.

        Args:
            size (int): The side length of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The unique ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A formatted string representing the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
