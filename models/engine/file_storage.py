#!/usr/bin/python3
"""
This is a module that contains a class for managing objects,
and persisting them to a JSON file.
The FileStorage class provides methods;
for adding, saving, and reloading objects.

Usage:
    To use this module,
    you can create an instance of the FileStorage class
    and use its methods to manage and persist objects to a JSON file.

Example:
    storage = FileStorage()
    obj = SomeObject()
    storage.new(obj)
    storage.save()
    storage.reload()

"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    A class for managing objects and persisting them to a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary to hold objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: The object to be added.

        Returns:
            None
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        dictionary = self.all()
        dictionary[key] = obj

    def save(self):
        """
        Save the objects to the JSON file.

        Returns:
            None
        """
        objs_dicts = {}

        for key in self.__objects.keys():
            obj = self.__objects.get(key)

            objs_dicts[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(objs_dicts, f)

    def reload(self):
        """
        Reload objects from the JSON file.

        If the file does not exist, it does nothing.

        Returns:
            None
        """
        try:
            with open(self.__file_path, "r") as f:
                objs_dicts = json.load(f)

                for obj_dict in objs_dicts.values():
                    class_name = obj_dict.get("__class__")
                    obj_dict.pop("__class__")

                    obj_class = globals()[class_name]
                    obj = obj_class(**obj_dict)

                    self.new(obj)
        except FileNotFoundError:
            pass
