#!/usr/bin/python3
""" Base model definition"""
from datetime import datetime
import uuid
from . import storage
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory', echo=True)



Base = declarative_base()

class BaseModel:
    """ Base model for other classes"""
    id = Column(String(60), primary_key=True)
    created_at = Column(String(), default=datetime.utcnow())
    updated_at = Column(String(), default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            if len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key != '__class__':
                        if key == "created_at" or key == "updated_at":
                            self.__dict__[key] = datetime.fromisoformat(value)

                        else:
                            self.__dict__[key] = value
            #else:

                #if key not in self.__dict__:
                #    storage.new(self)                    
            # self.create_at = self.__dict__.get("created_at")
            # self.id = self.__dict__.get("id")
            #    storage.new(self)
        #else:
        #    storage.new(self)


    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{BaseModel.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f'BaseModel')

    def save(self):
        """ Updates the public instance attr updated at """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Returns dictionary containing all key/values of __dict__ of the
        instance
        Args: no args
        """
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        
        for key, value in self.__dict__.items():
            if key == "created_at":
                created_at = self.__dict__["created_at"].isoformat()
            elif key == "updated_at":
                updated_at = self.__dict__["updated_at"].isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        
        if ("_sa_instance_state" in new_dict.keys()):
            del new_dict["_sa_instance_state"]
        return new_dict

    def __ne__(self, other):
        """ updates the updated_at if obj changes"""
        if self.__class__ != other.__class__:
            updated_at = datetime.now()

    def delete(self):
        """Deletes the current instance from storage"""
        storage.delete(self)
