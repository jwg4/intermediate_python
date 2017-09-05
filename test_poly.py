import unittest

from poly import Polynomial


class TestDisplayPoly(unittest.TestCase):
    def test_display_linear(self):
        p = Polynomial([1, 1])
        expected = "x + 1"
        self.assertEqual(str(p), expected)

    def test_display_cubic(self):
        p = Polynomial([1, 2, 2, 1])
        expected = "x**3 + 2x**2 + 2x + 1"
        self.assertEqual(str(p), expected)


class TestMultiplication(unittest.TestCase):
    def test_linear_times_linear(self):
        a = Polynomial([1, 1])
        b = Polynomial([3, 2])
        expected = Polynomial([3, 5, 2])
        self.assertEqual(a * b, expected)
        