s module defines tests for State class"""
import pycodestyle
import unittest
from models import city
from models.city import City


class TestCity(unittest.TestCase):
    """
    TestState class defines unit tests for City class
    """
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle error")

    def test_docstring(self):
        """Check for docstring presence"""
        self.assertIsNotNone(city.__doc__)
        self.assertIsNotNone(City.__doc__)

    def test_initialization(self):
        """Test with default value"""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")
        self.assertIsInstance(c.name, str)
        self.assertIsInstance(c.state_id, str)

    def test_attributes(self):
        """
        Test setting attributes of an instance and checking their values.
        """
        c = City()
        c.state_id = "123xyz"
        c.name = "Nairobi"
        self.assertEqual(c.state_id, "123xyz")
        self.assertEqual(c.name, "Nairobi")
        self.assertIsInstance(c.name, str)
        self.assertIsInstance(c.state_id, str)


if __name__ == '__main__':
    unittest.main()
