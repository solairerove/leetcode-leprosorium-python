import unittest

from dynamic_programming.PartitionEqualSubsetSum import can_partition


class MyTestCase(unittest.TestCase):
    def test_can_partition(self):
        self.assertEqual(True, can_partition(self, [1, 5, 11, 5]))  # add assertion here

    def test_can_partition_1(self):
        self.assertEqual(False, can_partition(self, [1, 2, 3, 5]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
