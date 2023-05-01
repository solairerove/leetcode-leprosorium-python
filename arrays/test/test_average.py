import unittest

from arrays.AverageSalaryExcludingTheMinimumAndMaximumSalary import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(2500.00000, average(self, [4000, 3000, 1000, 2000]))

    def test_average_1(self):
        self.assertEqual(2000.00000, average(self, [1000, 2000, 3000]))


if __name__ == '__main__':
    unittest.main()
