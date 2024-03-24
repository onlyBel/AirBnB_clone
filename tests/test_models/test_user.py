"""
This module defines tests for the User class
"""
import unittest
import pycodestyle
from models import user
from models.user import User


class TestUser(unittest.TestCase):
    """TestState class defines unit tests for the User class"""
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle error")

    def test_docstring(self):
        """Check for docstring presence"""
        self.assertIsNotNone(user.__doc__)
        self.assertIsNotNone(User.__doc__)

    def test_initialization(self):
        """
        Test the initialization of a User instance with default values.
        """
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_attributes(self):
        """
        Test setting attributes of a User instance and checking their values.
        """
        u = User()
        u.first_name = "Betty"
        u.last_name = "Bar"
        u.email = "airbnb@mail.com"
        u.password = "root"

        self.assertEqual(u.email, "airbnb@mail.com")
        self.assertEqual(u.password, "root")
        self.assertEqual(u.first_name, "Betty")
        self.assertEqual(u.last_name, "Bar")


if __name__ == '__main__':
    unittest.main()
