import unittest

from api import app

class GetBooksTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_true(self):
        self.assertEqual(123, 123)
