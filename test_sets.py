import unittest

from sets import multi_subsets, multi_subtract
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


class TestMultiSubsets(unittest.TestCase):
    def test_simple_multiset(self):
        m = {"a": 2}
        m_copy = m.copy()
        expected = [
            {"a": 2},
            {"a": 1},
            {}
        ]
        actual = list(multi_subsets(m))
        self.assertEqual(sorted(actual), sorted(expected))
        self.assertEqual(m, m_copy)


class TestMultiSubtract(unittest.TestCase):
    def test_simple_multisets(self):
        a = {'foo': 2, 'bar': 1, 'baz': 3}
        b = {'foo': 1, 'bar': 1}
        d = multi_subtract(a, b)
        e = {'foo': 1, 'baz': 3}
        self.assertEqual(d, e)
        
