import unittest

from dynamic_programming.DeleteAndEarn import delete_and_earn, delete_and_earn_top_down


class MyTestCase(unittest.TestCase):
    def test_delete_and_earn(self):
        self.assertEqual(6, delete_and_earn(self, [3, 4, 2]))
        self.assertEqual(6, delete_and_earn_top_down(self, [3, 4, 2]))

    def test_delete_and_earn_1(self):
        self.assertEqual(9, delete_and_earn(self, [2, 2, 3, 3, 3, 4]))
        self.assertEqual(9, delete_and_earn_top_down(self, [2, 2, 3, 3, 3, 4]))

    def test_delete_and_earn_2(self):
        self.assertEqual(18, delete_and_earn(self, [1, 1, 1, 2, 4, 5, 5, 5, 6]))
        self.assertEqual(18, delete_and_earn_top_down(self, [1, 1, 1, 2, 4, 5, 5, 5, 6]))


if __name__ == '__main__':
    unittest.main()
