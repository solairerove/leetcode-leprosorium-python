import unittest

from linked_list.RemoveDuplicatesFromSortedList import delete_duplicates, delete_duplicates_dumb
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_delete_duplicates(self):
        head = transform_array_to_list_node(self, [1, 1, 2])
        res = delete_duplicates(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1, 2], actual)

    def test_delete_duplicates_1(self):
        head = transform_array_to_list_node(self, [1, 1, 2, 3, 3])
        res = delete_duplicates(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1, 2, 3], actual)

    def test_delete_duplicates_2(self):
        head = transform_array_to_list_node(self, [1, 1, 1])
        res = delete_duplicates(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1], actual)

    def test_delete_duplicates_dumb(self):
        head = transform_array_to_list_node(self, [1, 1, 2])
        res = delete_duplicates_dumb(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1, 2], actual)

    def test_delete_duplicates_dumb_1(self):
        head = transform_array_to_list_node(self, [1, 1, 2, 3, 3])
        res = delete_duplicates_dumb(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1, 2, 3], actual)

    def test_delete_duplicates_dumb_2(self):
        head = transform_array_to_list_node(self, [1, 1, 1])
        res = delete_duplicates_dumb(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1], actual)


if __name__ == '__main__':
    unittest.main()
