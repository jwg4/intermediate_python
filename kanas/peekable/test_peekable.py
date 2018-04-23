import unittest

from . import peekable


class TestPeekableInterface(unittest.TestCase):
    def test_ctor(self):
        l = [1, 2, 3]
        p = peekable.PeekableInterface(l)
        self.assertIsNotNone(p)
    
    def test_next(self):
        l = [1, 2, 3]
        p = peekable.PeekableInterface(l)
        self.assertEqual(l.next(), p.next())