import unittest

from linked_list.MergeTwoSortedLists import merge_two_lists
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_merge_two_lists(self):
        list1 = transform_array_to_list_node(self, [1, 2, 4])
        list2 = transform_array_to_list_node(self, [1, 3, 4])
        res = merge_two_lists(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 1, 2, 3, 4, 4], actual)


if __name__ == '__main__':
    unittest.main()
