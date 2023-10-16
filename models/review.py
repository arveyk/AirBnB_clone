#!/usr/bin/python3
""" review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review model"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """ Child class init method"""
        super()__init__(self)
