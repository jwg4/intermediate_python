import unittest

from poly import Polynomial


class TestDisplayPoly(unittest.TestCase):
    def test_display_linear(self):
        p = Polynomial([1, 1])
        expected = "x + 1"
        self.assertEqual(str(p), expected)
