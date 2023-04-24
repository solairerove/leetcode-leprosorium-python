import unittest

from heap.LastStoneWeight import last_stone_weight


class MyTestCase(unittest.TestCase):
    def test_last_stone_weight(self):
        self.assertEqual(1, last_stone_weight(self, [2, 7, 4, 1, 8, 1]))

    def test_last_stone_weight_1(self):
        self.assertEqual(1, last_stone_weight(self, [1]))


if __name__ == '__main__':
    unittest.main()
