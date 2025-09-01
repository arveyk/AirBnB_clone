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

    def __init__(self, *args, **kwargs):
        """Initializes the instances/object of the User class
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{User.__name__}] ({self.id}) ({self.__dict__})")
 
    def __repr__(self): 
        """Return the Official representation of a class"""
        return (f'User')
