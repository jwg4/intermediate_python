import unittest

from approximants import root_convergents, pell_approximation
from approximants import fundamental_solution, is_not_square


class TestRootConvergents(unittest.TestCase):
    def test_first_approximation_to_root_2(self):
        generator = root_convergents(2)
        x = generator.next()
        self.assertEqual(x, (1, 1))

    def test_first_approximation_to_root_7(self):
        generator = root_convergents(7)
        x = generator.next()
        self.assertEqual(x, (2, 1))

    def test_third_approximation_to_root_7(self):
        generator = root_convergents(7)
        generator.next()
        generator.next()
        x = generator.next()
        self.assertEqual(x, (5, 2))


class TestPellApproximation(unittest.TestCase):
    def test_third_approximation_to_root_7(self):
        self.assertEqual(pell_approximation(7, 5, 2), -3)


class TestFundamentalSolution(unittest.TestCase):
    def test_solution_for_7(self):
        self.assertEqual(fundamental_solution(7), (8, 3))

    def test_solution_for_8(self):
        self.assertEqual(fundamental_solution(8), (3, 1))

    def test_solution_for_61(self):
        self.assertEqual(fundamental_solution(61), (1766319049, 226153980))


class TestIsNotSquare(unittest.TestCase):
    def test_up_to_100(self):
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        result = [ x for x in range(1, 101) if not is_not_square(x) ]
        self.assertEqual(result, expected)
