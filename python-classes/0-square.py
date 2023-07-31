class Square:
    def __init__(self, size):
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        # Attempting to access the private attribute directly
        print(my_square.size)
    except Exception as e:
        print(e)  # Output: 'Square' object has no attribute 'size'

    try:
        # Attempting to access the private attribute directly
        print(my_square.__size)
    except Exception as e:
        print(e)  # Output: 'Square' object has no attribute '__size'
