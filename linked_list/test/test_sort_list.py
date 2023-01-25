import unittest

from linked_list.SortList import sort_list
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_sort_list(self):
        head = transform_array_to_list_node(self, [4, 2, 1, 3])
        res = sort_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 3, 4], actual)

    def test_sort_list_1(self):
        head = transform_array_to_list_node(self, [-1, 5, 3, 4, 0])
        res = sort_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([-1, 0, 3, 4, 5], actual)

    def test_sort_list_2(self):
        head = transform_array_to_list_node(self, [6, 5, 3, 1, 8, 7, 2, 4])
        res = sort_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], actual)

    def test_sort_list_3(self):
        head = transform_array_to_list_node(self, [1])
        res = sort_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1], actual)

    def test_sort_list_4(self):
        head = transform_array_to_list_node(self, [1, 2])
        res = sort_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2], actual)

    def test_sort_list_5(self):
        head = transform_array_to_list_node(self, [2, 1])
        res = sort_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2], actual)


if __name__ == '__main__':
    unittest.main()
