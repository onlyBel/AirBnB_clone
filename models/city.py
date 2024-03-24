#!/usr/bin/python3
"""This a module that defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a specific city

    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
