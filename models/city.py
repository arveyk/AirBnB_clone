#!/usr/bin/python3
""" Class City """

from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""
    state_id = ""
    name = ""

    def __init__(self):
        """ Init of child class"""
        super().__init__()

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{City.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"City")
