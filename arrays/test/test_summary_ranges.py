import unittest

from arrays.SummaryRanges import summary_ranges


class MyTestCase(unittest.TestCase):
    def test_summary_ranges(self):
        self.assertEqual(["0->2", "4->5", "7"], summary_ranges(self, [0, 1, 2, 4, 5, 7]))

    def test_summary_ranges_1(self):
        self.assertEqual(["0", "2->4", "6", "8->9"], summary_ranges(self, [0, 2, 3, 4, 6, 8, 9]))


if __name__ == '__main__':
    unittest.main()
