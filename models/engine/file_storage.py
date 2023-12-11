#!/usr/bin/python3
"""Defines a class to manage file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serialize instance to JSON file and deserialize JSON file to instance
    Attributes:
    __file_path (str): The name of the file with saved objects.
     __objects (dict): A dictionary of serialised instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary objects in current storage."""
        return FileStorage.__objects

    def new(self, obj):
        """adds a new object to storage dictionary"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Saves JSON object to file"""
        o_dict = FileStorage.__objects
        dict_object = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_object, f)

    def reload(self):
        """reloads storage dictionary to file storage."""
        try:
            with open(FileStorage.__file_path) as f:
                dict_object = json.load(f)
                for i in dict_object.values():
                    clas = i["__class__"]
                    del i["__class__"]
                    self.new(eval(clas)(**i))
        except FileNotFoundError:
            return
