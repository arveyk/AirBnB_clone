#!/usr/bin/python3
""" User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines a User with some credentials
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """Initializes the instances/object of the User class
        """
