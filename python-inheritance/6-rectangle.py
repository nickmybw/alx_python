"""ALX task 6"""
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
