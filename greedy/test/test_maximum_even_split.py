import unittest

from greedy.MaximumSplitOfPositiveEvenIntegers import maximum_even_split


class MyTestCase(unittest.TestCase):
    def test_maximum_even_split(self):
        self.assertEqual([2, 4, 6], maximum_even_split(self, 12))

    def test_maximum_even_split_1(self):
        self.assertEqual([], maximum_even_split(self, 7))

    def test_maximum_even_split_2(self):
        self.assertEqual([2, 4, 6, 16], maximum_even_split(self, 28))


if __name__ == '__main__':
    unittest.main()
