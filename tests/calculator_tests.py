import unittest

from modules.calculator import add, sub, divide, multiply

class TestCalc(unittest.TestCase):

    def test_can_add(self):
     self.assertEqual(5, add(2,3))

    def test_can_sub(self):
     self.assertEqual(4, sub(8,4))

    def test_can_divide(self):
        self.assertEqual(3, divide(6,2))

    def test_can_multiply(self):
        self.assertEqual(12, multiply(4,3))