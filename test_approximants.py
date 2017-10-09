import unittest

from approximants import root_convergents


class TestRootConvergents(unittest.TestCase):
    def test_first_approximation_to_root_2(self):
        generator = root_convergents(2)
        x = generator.next()
        self.assertEqual(x, (1, 1))

    def test_first_approximation_to_root_7(self):
        generator = root_convergents(7)
        x = generator.next()
        self.assertEqual(x, (2, 1))

    def test_third_approximation_to_root_7(self):
        generator = root_convergents(7)
        generator.next()
        generator.next()
        x = generator.next()
        self.assertEqual(x, (5, 2))
