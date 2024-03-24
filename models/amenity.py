#!/usr/bin/python3
"""This is a module thatdefines the class amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents a specific amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
