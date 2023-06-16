import unittest

from trees.NumberOfWaysToReorderArrayToGetSameBST import num_of_ways


class MyTestCase(unittest.TestCase):
    def test_num_of_ways(self):
        self.assertEqual(1, num_of_ways(self, [2, 1, 3]))

    def test_num_of_ways_1(self):
        self.assertEqual(5, num_of_ways(self, [3, 4, 5, 1, 2]))

    def test_num_of_ways_2(self):
        self.assertEqual(0, num_of_ways(self, [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
