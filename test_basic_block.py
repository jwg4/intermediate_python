from unittest import TestCase


from basic_block import BasicBlock


class TestBasicBlock(TestCase):
    def setUp(self):
        self.counter = BasicBlock(1000)
 
    def test_top_number(self):
        self.assertEqual(self.counter.top_number(2), 1000)
