import unittest

from binary_search.SuccessfulPairsOfSpellsAndPotions import successful_pairs


class MyTestCase(unittest.TestCase):
    def test_successful_pairs(self):
        self.assertEqual([4, 0, 3], successful_pairs(self, [5, 1, 3], [1, 2, 3, 4, 5], 7))

    def test_successful_pairs_1(self):
        self.assertEqual([2, 0, 2], successful_pairs(self, [3, 1, 2], [8, 5, 8], 16))


if __name__ == '__main__':
    unittest.main()
