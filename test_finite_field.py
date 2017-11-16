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

    def test_multiplication(self):
        a = self.ff.FFPoint(3)
        b = self.ff.FFPoint(4)
        expected = self.ff.FFPoint(2)
        self.assertEqual(a * b, expected)

    def test_division(self):
        a = self.ff.FFPoint(2)
        b = self.ff.FFPoint(4)
        expected = self.ff.FFPoint(3)
        self.assertEqual(a / b, expected)

class TestModEleven(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ff = FiniteField(11)

    def test_addition(self):
        a = self.ff.FFPoint(3)
        b = self.ff.FFPoint(4)
        expected = self.ff.FFPoint(7)
        self.assertEqual(a + b, expected)

    def test_multiplication(self):
        a = self.ff.FFPoint(3)
        b = self.ff.FFPoint(4)
        expected = self.ff.FFPoint(1)
        self.assertEqual(a * b, expected)

    def test_division(self):
        a = self.ff.FFPoint(2)
        b = self.ff.FFPoint(4)
        expected = self.ff.FFPoint(6)
        self.assertEqual(a / b, expected)
