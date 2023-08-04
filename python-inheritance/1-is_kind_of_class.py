"""ALX Python- Inheritance Task 1"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare the object against.
    :return: True if the object is an instance of the specified class or its subclass; otherwise False.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    # You can add some test cases here to verify the function's functionality.
    pass
