import unittest

from linked_list.DeleteTheMiddleNodeOfALinkedList import delete_middle
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_delete_middle(self):
        head = transform_array_to_list_node(self, [1, 3, 4, 7, 1, 2, 6])
        delete_middle(self, head)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([1, 3, 4, 1, 2, 6], actual)

    def test_delete_middle_1(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4])
        delete_middle(self, head)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([1, 2, 4], actual)

    def test_delete_middle_2(self):
        head = transform_array_to_list_node(self, [2, 1])
        delete_middle(self, head)
        actual = transform_list_node_to_array(self, head)

        self.assertEqual([2], actual)


if __name__ == '__main__':
    unittest.main()
