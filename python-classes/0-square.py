class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

print(my_square.area())

my_square.__size = 5
print(my_square.area())
