#!/usr/bin/python3
""" Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Place """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        """init method"""
        super().__init__()

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{City.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"City")
