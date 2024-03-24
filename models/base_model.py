#!/usr/bin/python3
"""This is amodule that contains the definition of the class BaseModel"""

from datetime import datetime
import models
import json
import uuid


class BaseModel:
    """The base model for other classes in this project"""

    def __init__(self, *args, **kwargs):
        """Initializes a newly instantiated BaseModel object
        Args:
            args (tuple): a tuple of containing all the arguments to __init__()
            kwargs (dict): a dict of all the arguments by key/value
        Attributes:
            id (str): A unique id of the new instance
            created_at (datetime.datetime): the datetime the object was created
            updated_at (datetime.datetime): the datetime the object was updated
        """

        if kwargs and len(kwargs) > 0:
            for key in kwargs.keys():
                if type(key) is str and key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        kwargs[key] = datetime.fromisoformat(kwargs[key])
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a formatted string representation of the calling
        BaseModel instance
        """

        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`
        to the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a modified dict containing the attributes of the
        calling BaseModel instance
        """

        revised_dict = self.__dict__.copy()
        revised_dict.update({"__class__": type(self).__name__})
        revised_dict["created_at"] = self.created_at.isoformat()
        revised_dict["updated_at"] = self.updated_at.isoformat()

        return revised_dict
