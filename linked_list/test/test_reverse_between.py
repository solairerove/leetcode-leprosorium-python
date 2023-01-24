import unittest

from linked_list.ReverseLinkedListII import reverse_between
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_reverse_between(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = reverse_between(self, head, 2, 4)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 4, 3, 2, 5], actual)

    def test_reverse_between_1(self):
        head = transform_array_to_list_node(self, [5])
        res = reverse_between(self, head, 1, 1)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([5], actual)


if __name__ == '__main__':
    unittest.main()
