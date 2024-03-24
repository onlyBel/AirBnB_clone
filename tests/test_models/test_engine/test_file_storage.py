"""Unit test for tclass FileStorage"""

import os
import json
import unittest
import pycodestyle
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Tests the full functionality of the class FileStorage"""

    def test_pycodestyle(self):
        """Test that class FileStorage code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code pycodestyle errors.")

    def test_docstrings(self):
        """Tests that module file_storage and all its classes and functions are
        are properly documented
        """
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.all.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.new.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.save.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.reload.__doc__)

    def test_file_path_private(self):
        """Tests that `__file_path` is indeed a private attribute"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)
            print(FileStorage._file_path)
            print(FileStorage.file_path)

    def test_file_path_type(self):
        """Tests that private attribute `__file_path` is of type str"""
        self.assertTrue(type(FileStorage._FileStorage__file_path), str)

    def test_object_private(self):
        """Tests that `__object` is indeed a private attribute"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)
            print(FileStorage._objects)
            print(FileStorage.objects)

    def test_object_type(self):
        """Tests that private attribute `__object` is of type dict"""
        self.assertTrue(type(FileStorage._FileStorage__objects), dict)

    # def test_initially_empty_object(self):
    #     """Tests that `__object` is initially empty before calling method
    #     `reload()` on the FileStorage instance"""
    #     file_storage = FileStorage()
    #     self.assertEqual(len(file_storage.all()), 0)

    def test_method_all_returns_dict(self):
        """Tests that public instance method, all(), returns a dict"""
        file_storage = FileStorage()
        all_objects = file_storage.all()

        self.assertTrue(type(all_objects), dict)

    def test_method_all_return_value(self):
        """Tests that the return value of `all()` is actually `__objects`"""
        file_storage = FileStorage()
        all_objects = file_storage.all()
        self.assertIs(file_storage._FileStorage__objects, all_objects)

    def test_method_new_adds_obj_dict(self):
        """Tests that public instance method, new(), adds a new object
        to `__objects`, and confirms the key/value format
        """
        file_storage = FileStorage()
        objs = file_storage.all()
        objs_len = len(objs)

        bm = BaseModel()
        bm_key = f"{bm.__class__.__name__}.{bm.id}"

        last_added_obj = objs.copy().popitem()

        self.assertEqual(len(objs), objs_len + 1)
        self.assertEqual(last_added_obj[0], bm_key)
        self.assertEqual(last_added_obj[1], bm)

    def test_method_save(self):
        """Tests that the public instance method `save()` sends the JSON
        format of `__objects` to the file in the attribute `__file_path`"""
        objs = storage.all().copy()
        bm = BaseModel()

        updt_objs = storage.all().copy()

        self.assertEqual(len(updt_objs), len(objs) + 1)

        storage.save()
        storage.reload()

        rld_objs = storage.all()
        self.assertEqual(rld_objs.keys(), updt_objs.keys())
