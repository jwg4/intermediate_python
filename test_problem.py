import unittest

from poly import Polynomial
from problem import combine_w_symmetry
from problem import split_by_height
from problem import split_set
from problem import split_set_one
from problem import split_smart


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
            [ [a, a, b], [b], False ],
            [ [a, b, b], [a], False ],
            [ [a, a, b, b], [], False ],
        ]
        actual = list(split_set_one(polys))
        self.assertEqual(sorted(actual), sorted(expected))
        self.assertEqual(list(split_set_one(polys)), expected)


class TestSplitSmart(unittest.TestCase):
    def test_split_height_one(self):
        a = "a"
        b = "b"
        polys = [a, b]
        self.assertEqual(
            list(split_smart(polys, 1)),
            list(split_set_one(polys))
        )

    def test_split_height_two(self):
        a = "a"
        b = "b"
        polys = [a, b]
        self.assertEqual(
            list(split_smart(polys, 2)),
            list(split_set(polys))
        )


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
