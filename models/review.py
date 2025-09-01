#!/usr/bin/python3
""" review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review model"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Child class init method"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{Review.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"Review")
