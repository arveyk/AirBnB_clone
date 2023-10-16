#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Amenity class."""
=======
""" Aminities class"""
>>>>>>> b4ce5c1c752b82ad9481d4415a3ba5b59d9132a5
from models.base_model import BaseModel


class Amenity(BaseModel):
<<<<<<< HEAD
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
=======
    """ Amenities available to customer"""
    name = ""
    
    def __init__(self):
        super().__init__()
        pass

>>>>>>> b4ce5c1c752b82ad9481d4415a3ba5b59d9132a5
