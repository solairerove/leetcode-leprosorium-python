import unittest

from graphs.EvaluateDivision import calc_equation


class MyTestCase(unittest.TestCase):
    def test_calc_equation(self):
        self.assertEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
                         calc_equation(self, equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                       queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

    def test_calc_equation_1(self):
        self.assertEqual([3.75000, 0.40000, 5.00000, 0.20000],
                         calc_equation(self, equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                                       queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))

    def test_calc_equation_2(self):
        self.assertEqual([0.50000, 2.00000, -1.00000, -1.00000],
                         calc_equation(self, equations=[["a", "b"]], values=[0.5],
                                       queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))


if __name__ == '__main__':
    unittest.main()
