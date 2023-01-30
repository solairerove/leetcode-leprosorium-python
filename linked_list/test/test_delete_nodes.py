import unittest

from linked_list.DeleteNNodesAfterMNodesOfALinkedList import delete_nodes
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_delete_nodes(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        delete_nodes(self, head, 2, 3)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([1, 2, 6, 7, 11, 12], actual)

    def test_delete_nodes_1(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        delete_nodes(self, head, 1, 3)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([1, 5, 9], actual)


if __name__ == '__main__':
    unittest.main()
