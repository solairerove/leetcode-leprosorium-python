import unittest

from linked_list.ReverseLinkedList import reverse_list
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_reverse_linked_list(self):
        head = transform_array_to_list_node(self, [5, 2, 13, 3, 8])
        res = reverse_list(self, head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([8, 3, 13, 2, 5], actual)


if __name__ == '__main__':
    unittest.main()
