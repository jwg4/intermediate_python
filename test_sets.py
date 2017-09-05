import unittest

from sets import subsets_k
from sets import subsets_no_more_than


class TestSubsetsNoMoreThan(unittest.TestCase):
    def test_set_of_three(self):
        s = ["a", "b", "c"]
        expected = [
            [],
            ["a"],
            ["b"],
            ["c"],
        ]
        actual = list(subsets_no_more_than(s))
        self.assertEqual(sorted(actual), sorted(expected))

class TestSubsetsK(unittest.TestCase):
    def test_set_of_three(self):
        s = ["a", "b", "c"]
        expected = [
            ["a"],
            ["b"],
            ["c"],
        ]
        actual = list(subsets_k(s, 1))
        self.assertEqual(sorted(actual), sorted(expected))
