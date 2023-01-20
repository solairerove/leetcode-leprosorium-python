import unittest

from linked_list.RemoveNodesFromLinkedList import remove_nodes
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_remove_nodes_from_linked_list(self):
        head = transform_array_to_list_node(self, [5, 2, 13, 3, 8])
        res = remove_nodes(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([13, 8], actual)


if __name__ == '__main__':
    unittest.main()
