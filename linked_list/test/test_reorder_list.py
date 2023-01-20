import unittest

from linked_list.ReorderList import reorder_list
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_reorder_list(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4])
        reorder_list(self, head)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([1, 4, 2, 3], actual)

    def test_reorder_list_2(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        reorder_list(self, head)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([1, 5, 2, 4, 3], actual)


if __name__ == '__main__':
    unittest.main()
