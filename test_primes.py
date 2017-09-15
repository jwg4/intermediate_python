from unittest import TestCase

from primes import calculate_primes_less_than, calculate_primes_between
from primes import can_test_to


class TestCalculatePrimesLessThan(TestCase):
    def test_small_limit(self):
        expected = [2, 3, 5, 7]
        self.assertEqual(calculate_primes_less_than(10), expected)


class TestCalculatePrimesBetween(TestCase):
    def test_basic_calculation(self):
        primes = [[2, 3], [5, 7]]
        expected = [11, 13, 17, 19]
        result = calculate_primes_between(11, 20, primes)
        self.assertEqual(result, expected)


class TestCanTestTo(TestCase):
    def test_small_number(self):
        self.assertEqual(can_test_to(10), 100)
