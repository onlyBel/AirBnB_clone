#!/usr/bin/python3
"""This a module that defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents the user.

    Attributes:
        email (string): - empty string
        password (string) - empty string
        first_name (string) - empty string
        last_name (string): - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
