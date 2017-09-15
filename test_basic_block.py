from unittest import TestCase


from basic_block import BasicBlock


class TestBasicBlock(TestCase):
    def setUp(self):
        self.counter = BasicBlock(1000)
 
    def test_top_number(self):
        self.assertEqual(self.counter.top_number(1), 1000)
        self.assertEqual(self.counter.top_number(2), 2000)
 
    def test_block_contains(self):
        self.assertEqual(self.counter.block_contains(657), 1)
        self.assertEqual(self.counter.block_contains(1000), 1)
