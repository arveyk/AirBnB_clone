#!/usr/bin/python3
""" state class """
from models.base_model import BaseModel


class State(BaseModel):
    """ States which state a user is in
    """
    name = " "

    def __init__(self):
        """ Child init method"""
        super().__init__(self)
