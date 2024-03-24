from datetime import datetime
import unittest
import uuid
import pycodestyle
from models import base_model
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code pycodestyle errors.")

    def test_docstring(self):
        self.assertIsNotNone(base_model.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__init__.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__str__.__doc__)
        self.assertIsNotNone(base_model.BaseModel.save.__doc__)
        self.assertIsNotNone(base_model.BaseModel.to_dict.__doc__)

    def test_id(self):
        M = BaseModel()
        self.assertTrue(isinstance(M.id, str))

        # Check if id is a valid UUID
        try:
            uuid.UUID(M.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_id_multiple(self):
        M1 = BaseModel()
        M2 = BaseModel()
        M3 = BaseModel()
        self.assertTrue(isinstance(M1.id, str))
        self.assertNotEqual(M1.id, M2.id)
        self.assertNotEqual(M2.id, M3.id)
        self.assertNotEqual(M3.id, M1.id)

    def test_created_at(self):
        M = BaseModel()

        self.assertTrue(isinstance(M.created_at, datetime))
        # Use a tolerance value to check if the datetimes are close
        tolerance = datetime.now() - M.created_at
        self.assertLessEqual(tolerance.total_seconds(), 1)

    def test_created_at_multiple(self):
        M1 = BaseModel()
        M2 = BaseModel()
        M3 = BaseModel()

        self.assertTrue(isinstance(M1.created_at, datetime))
        self.assertTrue(isinstance(M2.created_at, datetime))
        self.assertTrue(isinstance(M3.created_at, datetime))

        self.assertLess(M1.created_at, M2.created_at)
        self.assertLess(M2.created_at, M3.created_at)
        self.assertLess(M1.created_at, M3.created_at)

    def test_updated_at_with_current(self):
        M = BaseModel()

        tolerance = datetime.now() - M.updated_at
        self.assertLessEqual(tolerance.total_seconds(), 1)

    def test_updated_at_and_created_at_time_diff(self):
        M = BaseModel()
        self.assertTrue(isinstance(M.created_at, datetime))
        self.assertTrue(isinstance(M.updated_at, datetime))

        # define a tolerance for the time difference (seconds)
        tolerance = 1

        # calculate time difference
        time_diff = (M.updated_at - M.created_at).total_seconds()
        self.assertLessEqual(time_diff, tolerance)

    def test_updated_at_multiple(self):
        M1 = BaseModel()
        M2 = BaseModel()
        M3 = BaseModel()

        self.assertTrue(isinstance(M1.updated_at, datetime))
        self.assertTrue(isinstance(M2.updated_at, datetime))
        self.assertTrue(isinstance(M3.updated_at, datetime))

        self.assertLess(M1.updated_at, M2.updated_at)
        self.assertLess(M2.updated_at, M3.updated_at)
        self.assertLess(M1.updated_at, M3.updated_at)

    def test__str__(self):
        M = BaseModel()
        self.assertTrue(isinstance(M.__str__(), str))
        self.assertEqual(M.__str__(), f"[{type(M).__name__}] ({M.id}) {M.__dict__}")

    def test_save(self):
        M = BaseModel()

        M.save()
        # Use a tolerance value to check if the datetimes are close
        tolerance = datetime.now() - M.updated_at
        self.assertLessEqual(tolerance.total_seconds(), 1)

    def test_save_multiple(self):
        M = BaseModel()

        update1 = M.updated_at
        M.save()
        update2 = M.updated_at
        M.save()
        update3 = M.updated_at

        self.assertTrue(isinstance(update1, datetime))
        self.assertTrue(isinstance(update2, datetime))
        self.assertTrue(isinstance(update3, datetime))

        self.assertLess(update1, update2)
        self.assertLess(update2, update3)
        self.assertLess(update1, update3)

    def test_to_dict_method(self):
        M = BaseModel()

        M_json = M.to_dict()
        self.assertIsInstance(M_json, dict)
        self.assertIsInstance(M_json['created_at'], str)
        self.assertIsInstance(M_json['updated_at'], str)
        self.assertEqual(M_json['__class__'], 'BaseModel')
        self.assertEqual(M_json['id'], M.id)

    def test_kwargs_empty(self):
        M = BaseModel()

        self.assertIsInstance(M.id, str)
        self.assertIsInstance(M.created_at, datetime)
        self.assertIsInstance(M.updated_at, datetime)

    def test_kwargs_passed(self):
        M = BaseModel()
        M.name = "MY_First_Model"
        M.my_number = 98

        M_json = M.to_dict()

        new_M = BaseModel(**M_json)

        self.assertIsInstance(new_M.id, str)
        self.assertIsInstance(new_M.created_at, datetime)
        self.assertIsInstance(new_M.updated_at, datetime)
        self.assertEqual(new_M.name, "MY_First_Model")
        self.assertEqual(new_M.my_number, 98)
        # self.assertFalse(hasattr(new_M, '__class__'))



if __name__ == '__main__':
    unittest.main()
