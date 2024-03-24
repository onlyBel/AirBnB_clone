"""This moduel defines tests fot the state class"""
import pycodestyle
import unittest
from models import state
from models.state import State


class TestState(unittest.TestCase):
    """
    TestState class defines unit tests for City class
    """
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle error.")

    def test_docstring(self):
        """Check for docstring presence"""
        self.assertIsNotNone(state.__doc__)
        self.assertIsNotNone(State.__doc__)

    def test_initialization(self):
        """
        Test with default value
        """
        s = State()
        self.assertEqual(s.name, "")
        self.assertIsInstance(s.name, str)

    def test_attributes(self):
        """
        Test setting attributes of an instance and checking their values.
        """
        s = State()
        s.name = "California"
        self.assertEqual(s.name, "California")


if __name__ == '__main__':
    unittest.main()
