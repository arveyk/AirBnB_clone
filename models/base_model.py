#!/usr/bin/python3
""" Base class module"""

import datetime
import uuid


class BaseModel:
    """Defines the class from which other class will be defined"""

    def __init__(self):
        """Init method"""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now().isoformat())
        self.updated_at = str(datetime.datetime.now().isoformat())
        self.__dict__[__class__] = str(BaseModel.__name__)

    def __str__(self):
        '''prints details about the class'''
        return (f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}")

    def __repr__(self):
        """ Returns the formal repr method"""
        return f'{self.__class__.__name__}'

    def save(self):
        """Updates the pubic instance attr updated_at with current datetime"""
        def __ne__(self, other):
            if type(self.__name) != type(other):
                update_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictinary containing all keys/values of __dict__"""
        return self.__dict__
