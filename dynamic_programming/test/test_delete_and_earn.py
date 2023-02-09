import unittest

from dynamic_programming.DeleteAndEarn import delete_and_earn


class MyTestCase(unittest.TestCase):
    def test_delete_and_earn(self):
        self.assertEqual(6, delete_and_earn(self, [3, 4, 2]))

    def test_delete_and_earn_1(self):
        self.assertEqual(9, delete_and_earn(self, [2, 2, 3, 3, 3, 4]))


if __name__ == '__main__':
    unittest.main()
