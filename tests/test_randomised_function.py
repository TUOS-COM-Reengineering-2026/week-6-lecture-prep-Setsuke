import unittest
from unittest.mock import patch
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    @patch('lecture.randint')
    def test_returns_software(self, mock_randint):
        mock_randint.return_value = 3
        self.assertEqual('software', randomised_function())

    @patch('lecture.randint')
    def test_returns_engineering(self, mock_randint):
        mock_randint.return_value = 7
        self.assertEqual('engineering', randomised_function())