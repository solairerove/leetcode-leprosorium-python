import unittest

from linked_list.SwapNodesInPairs import swap_pairs
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_swap_pairs(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4])
        res = swap_pairs(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([2, 1, 4, 3], actual)

    def test_swap_pairs_1(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = swap_pairs(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([2, 1, 4, 3, 5], actual)

    def test_swap_pairs_2(self):
        self.assertEqual(None, swap_pairs(self, None))

    def test_swap_pairs_3(self):
        head = transform_array_to_list_node(self, [1])
        res = swap_pairs(self, head)
        actual = transform_list_node_to_array(self, res)
        self.assertEqual([1], actual)


if __name__ == '__main__':
    unittest.main()
