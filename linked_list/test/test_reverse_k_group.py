import unittest

from linked_list.ReverseNodesInKGroup import reverse_k_group
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_reverse_k_group(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = reverse_k_group(self, head, 2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([2, 1, 4, 3, 5], actual)

    def test_reverse_k_group_1(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = reverse_k_group(self, head, 3)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([3, 2, 1, 4, 5], actual)


if __name__ == '__main__':
    unittest.main()
