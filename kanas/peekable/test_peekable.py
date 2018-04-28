import unittest

from . import peekable


class TestPeekableInterface(unittest.TestCase):
    def test_ctor(self):
        l = [1, 2, 3]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertIsNotNone(p)

    def test_next_compare(self):
        l = [1, 2, 3]
        i1 = iter(l)
        i2 = iter(l)
        p = peekable.PeekableInterface(i1)
        self.assertEqual(i2.__next__(), p.__next__())

    def test_next_check_value(self):
        l = ["foo", "bar", "baz"]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertEqual(p.__next__(), "foo")

    def test_peek_and_check_value(self):
        l = ["Z", "YY"]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertEqual(p.peek(), "Z")
        self.assertEqual(p.__next__(), "Z")

    def test_peek_past_the_end_of_list(self):
        l = []
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertIsNone(p.peek())

    def test_peek_twice(self):
        l = ["Z", "YY"]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertEqual(p.peek(), "Z")
        self.assertEqual(p.peek(), "Z")
        self.assertEqual(p.__next__(), "Z")

    def test_peek_two_different_values(self):
        l = ["Z", "YY"]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertEqual(p.peek(), "Z")
        self.assertEqual(p.__next__(), "Z")
        self.assertEqual(p.peek(), "YY")
        self.assertEqual(p.__next__(), "YY")

    def test_has_next(self):
        l = ["foo", "bar", "baz"]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertTrue(p.hasNext())

    def test_has_next_end_of_iterator(self):
        l = ["foo", "bar", "baz"]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        p.__next__()
        p.__next__()
        p.__next__()
        self.assertFalse(p.hasNext())

    def test_has_next_empty_iterator(self):
        l = []
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertFalse(p.hasNext())
