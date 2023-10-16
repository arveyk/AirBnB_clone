#!/usr/bin/python3
""" Aminities class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenities available to customer"""
    name = ""
    
    def __init__(self):
        super().__init__(self)
        pass

