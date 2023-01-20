import unittest

from linked_list.ReverseNodesInEvenLengthGroups import reverse_even_length_groups
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_reverse_even_length_groups(self):
        head = transform_array_to_list_node(self, [5, 2, 6, 3, 9, 1, 7, 3, 8, 4])
        res = reverse_even_length_groups(head)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([5, 6, 2, 3, 9, 1, 4, 8, 3, 7], actual)


if __name__ == '__main__':
    unittest.main()
