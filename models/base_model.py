#!/usr/bin/python3
""" Base model definition"""
import datetime
import uuid


class BaseModel:
    """ Base model for other classes"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] = value

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{BaseModel.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return f('BaseModels')

    def save(self):
        """ Updates the public instance attr updated at """
        updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns dictionary containing all key/values of __dict__ of the
        instance
        Args: no args
        """
        new_dict = self.__dict__
        created_at = datetime.datetime.now().isoformat()
        updated_at = datetime.datetime.now().isoformat()
        new_dict['__class__'] = BaseModel.__name__
        new_dict['created_at'] = created_at
        new_dict['updated_at'] = updated_at
        return new_dict

    def __ne__(self, other):
        """ updates the updated_at if obj changes"""
        if self.__class__ != other.__class__:
            updated_at = datetime.datetime.now()
