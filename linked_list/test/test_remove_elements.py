import unittest

from linked_list.RemoveLinkedListElements import remove_elements
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_remove_elements(self):
        head = transform_array_to_list_node(self, [1, 2, 6, 3, 4, 5, 6])
        res = remove_elements(self, head, 6)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 3, 4, 5], actual)

    def test_remove_elements_1(self):
        self.assertEqual(None, remove_elements(self, None, 1))

    def test_remove_elements_2(self):
        head = transform_array_to_list_node(self, [7, 7, 7, 7])
        res = remove_elements(self, head, 7)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([], actual)


if __name__ == '__main__':
    unittest.main()
