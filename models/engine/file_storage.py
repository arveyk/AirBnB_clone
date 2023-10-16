#!/usr/bin/python3
""" File storage class"""


class FileStorage:
    """ stores instances in JSON format and deserializes them as well"""
    __file_path = ""
    __objects = {}

    def all(self):
        """ returns the dictionary representation of __objects"""
        return dict(__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>. id
        Args:
            obj - 
        Returns: no return value
        """
        __objects['{__object.class.name.id}'] = obj

    def save(self):
        """serielizes __objects to JSON  file"""
        openThe __file_path (use with)
        serialize

    def reload(self):
        """deserializes the JSON file to __objects only if __file_path exits
        Args: none
        Returns: no return value """
