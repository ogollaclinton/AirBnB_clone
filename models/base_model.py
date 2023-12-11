#!/usr/bin/python3
""" This is the Base class for AirBnB console
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """ initialize new instance of BaseModel with a unique id"""
        self.id = str(uuid4())
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, date_format)
                else:
                    self.__dict__[i] = j

        else:
            models.storage.new(self)

    def __str__(self):
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_object = self.__dict__.copy()
        dict_object["__class__"] = self.__class__.__name__
        dict_object["created_at"] = self.created_at.isoformat()
        dict_object["updated_at"] = self.updated_at.isoformat()
        return dict_object
