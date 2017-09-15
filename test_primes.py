from unittest import TestCase

from primes import calculate_primes_less_than, calculate_primes_between


class TestCalculatePrimesLessThan(TestCase):
    def test_small_limit(self):
        expected = [2, 3, 5, 7]
        self.assertEqual(calculate_primes_less_than(10), expected)
