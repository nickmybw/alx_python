"""ALX task 8"""

class BaseGeometry:
    """
    Base class representing the base geometry.

    This class will be used as a base class for other geometry-related classes.
    It does not contain any methods or attributes at the moment.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method should be implemented by the subclasses, as each specific geometry
        will have its own way of calculating the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer.

        :param name: The name of the value (a string).
        :param value: The value to be validated.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def area(self):
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        :return: A string describing the rectangle in the format "[Rectangle] <width>/<height>".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class representing a square.

    Inherits from Rectangle and contains a size attribute.
    """

    def __init__(self, size):
        """
        Initialize the Square with given size.

        :param size: The size of the square (positive integer).
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        :return: A string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
