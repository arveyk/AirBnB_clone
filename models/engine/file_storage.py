#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
# from ...models.user import User
# from ...models.base_model import BaseModel
# from ...models.state import State
# from ...models.city import City
# from ...models.place import Place
# from ...models.amenity import Amenity
# from ...models.review import Review

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        # odict = FileStorage.__objects
        # objdict = {
        # objKey: odict[objKey].to_dict() for objKey in odict.keys()}
        objdict = {
                objKey: FileStorage.__objects[objKey].to_dict()
                for objKey in FileStorage.__objects.keys()
                }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.place import Place
                from models.amenity import Amenity
                from models.review import Review

                for objAttributes in objdict.values():
                    cls_name = objAttributes["__class__"]
                    # del objAttributes["__class__"]
                    match cls_name:
                        case "Amenity":
                            self.new(Amenity(**objAttributes))
                        case "BaseModel":
                            self.new(BaseModel(**objAttributes))
                        case "City":
                            self.new(City(**objAttributes))
                        case "BaseModel":
                            self.new(BaseModel(**objAttributes))
                        case "Place":
                            self.new(Place(**objAttributes))
                        case "Review":
                            self.new(Review(**objAttributes))
                        case "User":
                            self.new(User(**objAttributes))
                comment = """for o in objdict.values():
                    cls_name = o["__class__"]
                    #del o["__class__"]
                    self.new(eval(cls_name)(**o))
                    """
        except FileNotFoundError:
            return
