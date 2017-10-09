import unittest

from approximants import root_convergents


class TestRootConvergents(unittest.TestCase):
    def test_first_approximation_to_root_2(self):
        generator = root_convergents(2)
        x = generator.next()
        self.assertEqual(x, (1, 1))
