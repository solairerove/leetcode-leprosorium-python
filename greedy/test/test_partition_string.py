import unittest

from greedy.OptimalPartitionOfString import partition_string


class MyTestCase(unittest.TestCase):
    def test_partition_string(self):
        self.assertEqual(4, partition_string(self, "abacaba"))

    def test_partition_string_1(self):
        self.assertEqual(6, partition_string(self, "ssssss"))


if __name__ == '__main__':
    unittest.main()
