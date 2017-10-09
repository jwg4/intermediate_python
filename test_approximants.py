import unittest

from approximants import root_convergents, pell_approximation, fundamental_solution


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
