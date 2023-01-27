import unittest

from linked_list.DeleteNodeInALinkedList import delete_node
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_delete_node(self):
        head = transform_array_to_list_node(self, [4, 5, 1, 9])
        delete_node(self, head.next)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([4, 1, 9], actual)

    def test_delete_node_1(self):
        head = transform_array_to_list_node(self, [4, 5, 1, 9])
        delete_node(self, head.next.next)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([4, 5, 9], actual)


if __name__ == '__main__':
    unittest.main()
