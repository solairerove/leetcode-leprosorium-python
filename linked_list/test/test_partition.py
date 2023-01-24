import unittest

from linked_list.PartitionList import partition
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_partition(self):
        head = transform_array_to_list_node(self, [1, 4, 3, 2, 5, 2])
        res = partition(self, head, 3)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 2, 4, 3, 5], actual)

    def test_partition_1(self):
        head = transform_array_to_list_node(self, [2, 1])
        res = partition(self, head, 2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2], actual)


if __name__ == '__main__':
    unittest.main()
