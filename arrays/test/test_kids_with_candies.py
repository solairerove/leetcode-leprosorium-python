import unittest

from arrays.KidsWithTheGreatestNumberOfCandies import kids_with_candies


class MyTestCase(unittest.TestCase):
    def test_kids_with_candies(self):
        self.assertEqual([True, True, True, False, True], kids_with_candies(self, [2, 3, 5, 1, 3], 3))

    def test_kids_with_candies_1(self):
        self.assertEqual([True, False, False, False, False], kids_with_candies(self, [4, 2, 1, 1, 2], 1))

    def test_kids_with_candies_2(self):
        self.assertEqual([True, False, True], kids_with_candies(self, [12, 1, 12], 10))


if __name__ == '__main__':
    unittest.main()
