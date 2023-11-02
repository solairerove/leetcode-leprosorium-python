import unittest

from arrays.SortColors import sort_colors


class MyTestCase(unittest.TestCase):
    def test_sort_colors(self):
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(self, nums=nums)
        self.assertEqual([0, 0, 1, 1, 2, 2], nums)

    def test_sort_colors_1(self):
        nums = [2, 0, 1]
        sort_colors(self, nums=nums)
        self.assertEqual([0, 1, 2], nums)


if __name__ == '__main__':
    unittest.main()
