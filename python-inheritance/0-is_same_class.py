"""ALX Python-Inheritance Task 0"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare the object against.
    :return: True if the object is exactly an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class


if __name__ == "__main__":
    # You can add some test cases here to verify the function's functionality.
    pass
