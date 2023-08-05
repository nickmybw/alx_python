"""ALX task 2"""
def inherits_from(obj, a_class):
    """Check if obj is an instance of class."""
    obj_class = type(obj)
    if issubclass(obj_class, a_class) and obj_class is not a_class:
        return True
    else:
        return False