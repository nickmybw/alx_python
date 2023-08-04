"""ALX task 4"""
class BaseGeometry:
    """
    A class representing a base geometry.

    This class can be used as a base for more specific geometry classes.
    """

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
