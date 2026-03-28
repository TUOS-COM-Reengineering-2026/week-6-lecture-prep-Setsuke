import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    def test_behaviour_1(self):
        self.assertEqual(
            strange_function(100, 100, -50, 0),
            'behaviour 1'
        )

    def test_behaviour_2(self):
        self.assertEqual(
            strange_function(7, 7, 10, 5),
            'behaviour 2'
        )

    def test_behaviour_4(self):
        self.assertEqual(
            strange_function(50, 10, 20, -5),
            'behaviour 4'
        )

    def test_behaviour_5(self):
        self.assertEqual(
            strange_function(30, 10, 5, 15),
            'behaviour 5'
        )

    def test_behaviour_6(self):
        self.assertEqual(
            strange_function(8, 3, 8, 10),
            'behaviour 6'
        )