#!/usr/bin/python3
"""Utilities class
"""
from models.base_model import BaseModel


class Util(BaseModel):
    name = ""
    def __init__(self):
        """Init for Util"""
        super().__init__()

    def __str__(self):
        """ prints unofficial representation of class"""
        return (f"[{Util.__name__}] ({self.id}) ({self.__dict__})")

    def __repr__(self):
        return (f"Util")
