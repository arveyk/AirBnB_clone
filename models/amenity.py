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
        super().__init__(self)
