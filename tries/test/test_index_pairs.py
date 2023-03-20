import unittest

from tries.IndexPairsOfAString import index_pairs


class MyTestCase(unittest.TestCase):
    def test_index_pairs(self):
        self.assertEqual([[3, 7], [9, 13], [10, 17]],
                         index_pairs(self, "thestoryofleetcodeandme", ["story", "fleet", "leetcode"]))

    def test_index_pairs_1(self):
        self.assertEqual([[0, 1], [0, 2], [2, 3], [2, 4]], index_pairs(self, "ababa", ["aba", "ab"]))


if __name__ == '__main__':
    unittest.main()
