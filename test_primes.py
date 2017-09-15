from unittest import TestCase

from primes import calculate_primes_less_than, calculate_primes_between
from primes import can_test_to, need_to_test


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
        self.assertEqual(can_test_to(10), 120)

    def test_round_trip(self):
        start = 1000
        primes_needed = need_to_test(start)
        limit = can_test_to(primes_needed)
        self.assertGreaterEqual(limit, start)

    def test_round_trip_2(self):
        limit = can_test_to(start)
        print limit
        primes_needed = need_to_test(limit)
        self.assertIn(primes_needed, [start, start+1])
