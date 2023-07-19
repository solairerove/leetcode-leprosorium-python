import unittest

from greedy.NonOverlappingIntervals import erase_overlap_intervals


class MyTestCase(unittest.TestCase):
    def test_erase_overlap_intervals(self):
        self.assertEqual(1, erase_overlap_intervals(self, intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))

    def test_erase_overlap_intervals_1(self):
        self.assertEqual(2, erase_overlap_intervals(self, intervals=[[1, 2], [1, 2], [1, 2]]))

    def test_erase_overlap_intervals_2(self):
        self.assertEqual(0, erase_overlap_intervals(self, intervals=[[1, 2], [2, 3]]))

        if __name__ == '__main__':
            unittest.main()
