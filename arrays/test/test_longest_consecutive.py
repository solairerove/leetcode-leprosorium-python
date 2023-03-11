import unittest

from arrays.LongestConsecutiveSequence import longest_consecutive


class MyTestCase(unittest.TestCase):
    def test_longest_consecutive(self):
        self.assertEqual(4, longest_consecutive(self, [100, 4, 200, 1, 3, 2]))

    def test_longest_consecutive_1(self):
        self.assertEqual(9, longest_consecutive(self, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


if __name__ == '__main__':
    unittest.main()
