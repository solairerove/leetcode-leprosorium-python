import unittest

from linked_list.RemoveDuplicatesFromSortedListII import delete_duplicates
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_delete_duplicates(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 3, 4, 4, 5])
        res = delete_duplicates(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 5], actual)

    def test_delete_duplicates_1(self):
        head = transform_array_to_list_node(self, [1, 1, 1, 2, 3])
        res = delete_duplicates(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([2, 3], actual)

    def test_delete_duplicates_2(self):
        head = transform_array_to_list_node(self, [1, 2, 2])
        res = delete_duplicates(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1], actual)


if __name__ == '__main__':
    unittest.main()
