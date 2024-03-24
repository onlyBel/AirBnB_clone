"""This module defines test for the review class"""
import pycodestyle
import unittest
from models import review
from models.review import Review


class TestReview(unittest.TestCase):
    """TestState class defines unit tests for the Review class"""
    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "pycodestyle error.")

    def test_docstring(self):
        """Check for docstring presence"""
        self.assertIsNotNone(review.__doc__)
        self.assertIsNotNone(Review.__doc__)

    def test_initialization(self):
        """Test with default value"""
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)

    def test_attributes(self):
        """
        Test setting attributes of an instance and checking their values.
        """
        r = Review()
        r.place_id = "123xyz"
        r.user_id = "123abc"
        r.text = "Hello, World!"

        self.assertEqual(r.place_id, "123xyz")
        self.assertEqual(r.user_id, "123abc")
        self.assertEqual(r.text, "Hello, World!")


if __name__ == '__main__':
    unittest.main()
