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