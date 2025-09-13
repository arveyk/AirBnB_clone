#!/usr/bin/python3
""" state class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ States which state a user is in
    """
    __tablename__ = "states"
    id = Column(String(60), primary_key=True)
    name = Column(String(128))
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ Child init method"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{State.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"State")
