import unittest

from poly import Polynomial
from problem import combine_w_symmetry
from problem import split_by_height
from problem import split_set
from problem import split_set_one


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


class TestSplitSetOne(unittest.TestCase):
    def test_split_two(self):
        polys = [
            Polynomial([1, 1, 1])
        ]
        expected = [
            [ [Polynomial([1, 1, 1])], [Polynomial([1, 1, 1])], True ],
            [ [Polynomial([1, 1, 1]), Polynomial([1, 1, 1])], [], False ],
        ]
        self.assertEqual(list(split_set_one(polys)), expected)

    def test_split_simple_two(self):
        polys = [
            "a"
        ]
        expected = [
            [ ["a"], ["a"], True ],
            [ ["a", "a"], [], False ],
        ]
        self.assertEqual(list(split_set_one(polys)), expected)


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
        sets = [ [ [["A"], ["A"], True] ] ]
        expected = [
            [ ["A"], ["A"] ]
        ]
        self.assertEqual(list(combine_w_symmetry(sets)), expected)

    def test_two_splits(self):
        sets = [
            [ [["A"], ["A"], True] ],
            [ [["B"], ["B"], True] ],
        ]
        expected = [
            [ ["A", "B"], ["A", "B"] ]
        ]
        self.assertEqual(list(combine_w_symmetry(sets)), expected)

    def test_two_splits_with_asymmetric(self):
        sets = [
            [ [["A"], ["A"], True] ],
            [ [["B"], ["~B"], False] ],
        ]
        expected = [
            [ ["A", "B"], ["A", "~B"] ],
        ]
        self.assertEqual(list(combine_w_symmetry(sets)), expected)

    def test_two_splits_with_both_asymmetric(self):
        sets = [
            [ [["A"], ["a"], False] ],
            [ [["B"], ["b"], False] ],
        ]
        expected = [
            [ ["A", "B"], ["a", "b"] ],
            [ ["A", "b"], ["a", "B"] ],
        ]
        self.assertEqual(list(combine_w_symmetry(sets)), expected)
