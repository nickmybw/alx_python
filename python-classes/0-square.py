class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.__dict__)

    mysquare = Square(89)
    print(type(mysquare))
    print(mysquare.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(mysquare._size)
    except Exception as e:
        print(e)
