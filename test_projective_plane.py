from finite_field import FiniteField
from projective_plane import ProjectivePlane

import unittest


class TestObjectBehavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pp = ProjectivePlane(
            FiniteField(5)
        )

    def test_two_equivalent_objects(self):
        first = self.pp(1, 2, 3)
        second = self.pp(4, 3, 2)
        self.assertEqual(first, second)
    
    def test_two_different_objects(self):
        first = self.pp(1, 2, 0)
        second = self.pp(4, 3, 2)
        self.assertNotEqual(first, second)
    
    def test_two_more_different_objects(self):
        first = self.pp(1, 2, 1)
        second = self.pp(4, 3, 2)
        self.assertNotEqual(first, second)
