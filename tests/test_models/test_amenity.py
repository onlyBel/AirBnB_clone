"""This isamodule thatdefines tests for amenity class"""
import pycodestyle
import unittest
from models import amenity
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestState class defines unit tests for Amenity class
    """
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle error")

    def test_docstring(self):
        """Check for docstring presence"""
        self.assertIsNotNone(amenity.__doc__)
        self.assertIsNotNone(Amenity.__doc__)

    def test_initialization(self):
        """Test with default value"""
        c = Amenity()
        self.assertEqual(c.name, "")
        self.assertIsInstance(c.name, str)

    def test_attributes(self):
        """
        Test setting attributes of an instance and checking their values.
        """
        c = Amenity()
        c.name = "Lagos"
        self.assertEqual(c.name, "Lagos")
        self.assertIsInstance(c.name, str)


if __name__ == '__main__':
    unittest.main()
