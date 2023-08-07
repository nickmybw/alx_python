"""ALX task 0"""
class Base:
    """
    Base class for managing the id attribute in all other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): If provided, assign it to the public instance attribute id.
                      Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
