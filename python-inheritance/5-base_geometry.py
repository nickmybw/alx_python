"""ALX task 5"""
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
