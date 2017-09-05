import unittest

from poly import Polynomial
from problem import combine_w_symmetry
from problem import split_by_height
from problem import split_set


class TestSplitByHeight(unittest.TestCase):
    def test_basic_split(self):
        polys = [
            Polynomial([1, 1, 1]),
            Polynomial([1, -1, 1])
        ]
        expected = {
            1: [ Polynomial([1, -1, 1]) ],
            3: [ Polynomial([1, 1, 1]) ]
        }
        self.assertEqual(
            split_by_height(polys),
            expected
        )


class TestSplitSet(unittest.TestCase):
    def test_split_two(self):
        polys = [
            Polynomial([1, 1, 1])
        ]
        expected = [
            [
                [Polynomial([1, 1, 1])],
                [Polynomial([1, 1, 1])],
                True
            ],
        ]
        self.assertEqual(list(split_set(polys)), expected)

    def test_split_four(self):
        a = "a"
        b = "b"
        polys = [a, b]
        expected = [
            [ [a, b], [a, b], True ],
            [ [a, a], [b, b], False ],
        ]
        self.assertEqual(list(split_set(polys)), expected)


class TestCombineWSymmetry(unittest.TestCase):
    def test_single_split(self):
        sets = [ [ ["A", "A", True] ] ]
        expected = [
            [ ["A"], ["A"] ]
        ]
        self.assertEqual(list(combine_w_symmetry(sets)), expected)
