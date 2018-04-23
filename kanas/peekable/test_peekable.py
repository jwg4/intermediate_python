import unittest

from . import peekable


class TestPeekableInterface(unittest.TestCase):
    def test_ctor(self):
        l = [1, 2, 3]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertIsNotNone(p)
    
    def test_next(self):
        l = [1, 2, 3]
        i = iter(l)
        p = peekable.PeekableInterface(i)
        self.assertEqual(i.__next__(), p.__next__())