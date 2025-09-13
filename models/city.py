#!/usr/bin/python3
""" Class City """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String
from models.state import State
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Class City"""
    __tablename__ = "cities"
    id = Column(String(60), primary_key=True)
    name = Column(String(128))
    state_id = Column(String(60), ForeignKey("states.id"))

    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        """ Init of child class"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{City.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"City")
