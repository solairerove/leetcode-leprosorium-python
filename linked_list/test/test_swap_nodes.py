import unittest

from linked_list.SwappingNodesInALinkedList import swap_nodes
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_swap_nodes(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = swap_nodes(self, head, 2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 4, 3, 2, 5], actual)

    def test_swap_nodes_1(self):
        head = transform_array_to_list_node(self, [7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
        res = swap_nodes(self, head, 5)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([7, 9, 6, 6, 8, 7, 3, 0, 9, 5], actual)


if __name__ == '__main__':
    unittest.main()
