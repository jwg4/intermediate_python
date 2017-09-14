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
    def setUp(self):
        def compare(a, b, msg=None):
            if a != b:
                if msg is None:
                    msg = "%s != %s" % (repr(a), repr(b))
                raise self.failureException(msg)
        self.addTypeEqualityFunc(Polynomial, compare)

    def test_linear_times_linear(self):
        a = Polynomial([1, 1])
        b = Polynomial([3, 2])
        expected = Polynomial([3, 5, 2])
        self.assertEqual(a * b, expected)

    def test_linear_times_linear_2(self):
        a = Polynomial([1, 1])
        b = Polynomial([2, 2])
        expected = Polynomial([2, 4, 2])
        self.assertEqual(a * b, expected)


class TestIsPositive(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(Polynomial([1, 3, 4, 4, 3, 1]).is_positive)

    def test_negative(self):
        self.assertFalse(Polynomial([1, 3, -4, 4, 3, 1]).is_positive)


class TestPretty(unittest.TestCase):
    def test_quadratic_values(self):
        p = Polynomial([3, 5, 2])
        expected = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
        self.assertEqual(list(p.pretty_values), expected)

    def test_quadratic(self):
        p = Polynomial([3, 5, 2])
        expected = "(0, 0, 0, 1, 1, 1, 1, 1, 2, 2)"
        self.assertEqual(p.pretty, expected)
