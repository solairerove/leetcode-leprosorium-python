import unittest

from linked_list.MergeKSortedLists import merge_k_lists
from linked_list.test.utils import transform_list_node_to_array, transform_array_to_list_node


class MyTestCase(unittest.TestCase):
    def test_merge_k_lists(self):
        list1 = transform_array_to_list_node(self, [1, 4, 5])
        list2 = transform_array_to_list_node(self, [1, 3, 4])
        list3 = transform_array_to_list_node(self, [2, 6])
        res = merge_k_lists(self, [list1, list2, list3])
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], actual)


if __name__ == '__main__':
    unittest.main()
