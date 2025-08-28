#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenities available to customer

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

    def __init__(self):
        """Initializing function/method
        Args: None
        Return None
        """
        super().__init__()

     def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{City.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"City")
