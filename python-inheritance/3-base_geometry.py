"""Alx task 3"""
class BaseGeometry:
    """
    Empty class representing the base geometry.

    This class will be used as a base class for other geometry-related classes.
    It does not contain any methods or attributes at the moment.
    """
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__int_subclass__"]
        return new_attribute_list
    
    
