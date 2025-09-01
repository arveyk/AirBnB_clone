#!/usr/bin/python3
""" state class """
from models.base_model import BaseModel


class State(BaseModel):
    """ States which state a user is in
    """
    name = " "

    def __init__(self, *args, **kwargs):
        """ Child init method"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{State.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"State")
