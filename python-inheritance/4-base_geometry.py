"""ALX task 4"""


class BaseGeometryMeta(type):
    """BaseGeometryMeta description"""

    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [
            item for item in attributes if item != '__init_subclass__']
        return new_attribute_list


class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    Empty class representing the base geometry.

    This class will be used as a base class for other geometry-related classes.
    It does not contain any methods or attributes at the moment.
    """

    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [
            item for item in attributes if item != '__init_subclass__']
        return new_attribute_list

    def area(self):
        """
        Compute the area of the geometry.

        This method should be implemented in subclasses to calculate the area of the specific geometry.
        If not implemented, it raises an Exception with the message 'area() is not implemented'.

        :raises: Exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')


if __name__ == "__main__":
    # You can add some test cases here if needed.
    pass
