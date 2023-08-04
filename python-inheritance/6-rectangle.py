"""ALX task 6"""

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    Inherits from BaseGeometry and contains width and height attributes.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with given width and height.

        :param width: The width of the rectangle (positive integer).
        :param height: The height of the rectangle (positive integer).
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
