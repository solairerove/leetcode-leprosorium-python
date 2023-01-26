import unittest

from linked_list.OddEvenLinkedList import odd_even_list
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_odd_even_list(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = odd_even_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 3, 5, 2, 4], actual)

    def test_odd_even_list_1(self):
        head = transform_array_to_list_node(self, [2, 1, 3, 5, 6, 4, 7])
        res = odd_even_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([2, 3, 6, 7, 1, 5, 4], actual)

    def test_odd_even_list_32(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5, 6, 7, 8])
        res = odd_even_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 3, 5, 7, 2, 4, 6, 8], actual)


if __name__ == '__main__':
    unittest.main()
