from finite_field import FiniteField

import unittest


class TestModFive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ff = FiniteField(5)

    def test_addition(self):
        a = self.ff.FFPoint(3)
        b = self.ff.FFPoint(4)
        expected = self.ff.FFPoint(2)
        self.assertEqual(a + b, expected)
