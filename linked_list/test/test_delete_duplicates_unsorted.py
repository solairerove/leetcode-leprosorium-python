import unittest

from linked_list.RemoveDuplicatesFromAnUnsortedLinkedList import delete_duplicates_unsorted
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_delete_duplicates_unsorted(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 2])
        res = delete_duplicates_unsorted(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 3], actual)

    def test_delete_duplicates_unsorted_1(self):
        head = transform_array_to_list_node(self, [2, 1, 1, 2])
        res = delete_duplicates_unsorted(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([], actual)

    def test_delete_duplicates_unsorted_2(self):
        head = transform_array_to_list_node(self, [3, 2, 2, 1, 3, 2, 4])
        res = delete_duplicates_unsorted(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 4], actual)


if __name__ == '__main__':
    unittest.main()
