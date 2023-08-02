class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        self.__size = size


my_square = Square(3)
print(type(my_square))  # <class '__main__.Square'>
print(my_square.__dict__)  # {'_Square__size': 3}

try:
    print(my_square.size)
except Exception as e:
    print(e)  # 'Square' object has no attribute 'size'

try:
    print(my_square.__size)
except Exception as e:
    print(e)  # 'Square' object has no attribute '__size'
