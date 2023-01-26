import unittest

from linked_list.MiddleOfTheLinkedList import middle_node
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_middle_node(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = middle_node(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([3, 4, 5], actual)

    def test_middle_node_1(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5, 6])
        res = middle_node(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([4, 5, 6], actual)


if __name__ == '__main__':
    unittest.main()
