import unittest

from arrays.PartitionLabels import partition_labels


class MyTestCase(unittest.TestCase):
    def test_partition_labels(self):
        self.assertEqual([9, 7, 8], partition_labels(self, s="ababcbacadefegdehijhklij"))

    def test_partition_labels_1(self):
        self.assertEqual([10], partition_labels(self, s="eccbbbbdec"))


if __name__ == '__main__':
    unittest.main()
