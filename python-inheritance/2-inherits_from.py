"""ALX Python Inheritance Task 2"""

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare the object against.
    :return: True if the object is an instance of a class that inherited from the specified class; otherwise False.
    """
    return isinstance(obj, type) and issubclass(obj, a_class) and obj != a_class


"""ALX Python-Inheritance Task 2"""

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class;
    otherwise False.
    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a class that inherited from a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

