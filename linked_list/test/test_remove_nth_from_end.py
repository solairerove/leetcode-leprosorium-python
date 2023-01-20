import unittest

from linked_list.RemoveNthNodeFromEndOfList import remove_nth_from_end
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_remove_nth_from_end(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = remove_nth_from_end(self, head, 2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 3, 5], actual)


if __name__ == '__main__':
    unittest.main()
