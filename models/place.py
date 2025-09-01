#!/usr/bin/python3
""" Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Place """
    amenity_ids = []
    city_id = ""
    latitude = 0.0
    longitude = 0.0
    description = ""
    max_guests = 0
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    user_id = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{Place.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"Place")
