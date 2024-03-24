#!/usr/bin/python3

"""This module contains function module_import()"""


def module_import():
    """Create an instance of the class FileStorage"""
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
    return storage


global storage
storage = module_import()
