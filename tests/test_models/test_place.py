"""This module defines tests for Place class"""
import pycodestyle
import unittest
from models import place
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    TestState class defines unit tests for Place class
    """
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle error")

    def test_docstring(self):
        """Check for docstring presence"""
        self.assertIsNotNone(place.__doc__)
        self.assertIsNotNone(Place.__doc__)

    def test_initialization(self):
        """Test with default value"""
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)

    def test_attributes(self):
        """
        Test setting attributes of an instance and checking their values.
        """
        p = Place()
        p.city_id = "123xyz"
        p.user_id = "abc123"
        p.name = "Betty"
        p.description = "Hello, World!"
        p.number_rooms = 98
        p.number_bathrooms = 69
        p.price_by_night = 200
        p.max_guest = 7
        p.longitude = 5.5
        p.latitude = 7.9
        p.amenity_ids = []

        self.assertEqual(p.city_id, "123xyz")
        self.assertEqual(p.user_id, "abc123")
        self.assertEqual(p.name, "Betty")
        self.assertEqual(p.description, "Hello, World!")
        self.assertEqual(p.number_rooms, 98)
        self.assertEqual(p.number_bathrooms, 69)
        self.assertEqual(p.price_by_night, 200)
        self.assertEqual(p.max_guest, 7)
        self.assertEqual(p.longitude, 5.5)
        self.assertEqual(p.latitude, 7.9)
        self.assertEqual(p.amenity_ids, [])

        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
