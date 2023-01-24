import unittest

from linked_list.RotateList import rotate_right
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_rotate_right(self):
        head = transform_array_to_list_node(self, [1, 2, 3, 4, 5])
        res = rotate_right(self, head, 2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([4, 5, 1, 2, 3], actual)

    def test_rotate_right_1(self):
        head = transform_array_to_list_node(self, [0, 1, 2])
        res = rotate_right(self, head, 4)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([2, 0, 1], actual)

    def test_rotate_right_2(self):
        head = transform_array_to_list_node(self, [1, 2])
        res = rotate_right(self, head, 0)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2], actual)

    def test_rotate_right_3(self):
        head = transform_array_to_list_node(self, [1, 2])
        res = rotate_right(self, head, 2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2], actual)


if __name__ == '__main__':
    unittest.main()
