import unittest

from linked_list.AddTwoNumbersII import add_two_numbers_naive_ii, add_two_numbers_stack_ii, add_two_numbers_ii
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_add_two_numbers_naive(self):
        list1 = transform_array_to_list_node(self, [7, 2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers_naive_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([7, 8, 0, 7], actual)

    def test_add_two_numbers_naive_1(self):
        list1 = transform_array_to_list_node(self, [2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers_naive_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([8, 0, 7], actual)

    def test_add_two_numbers_naive_2(self):
        list1 = transform_array_to_list_node(self, [0])
        list2 = transform_array_to_list_node(self, [0])
        res = add_two_numbers_naive_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([0], actual)

    def test_add_two_numbers_stack(self):
        list1 = transform_array_to_list_node(self, [7, 2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers_stack_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([7, 8, 0, 7], actual)

    def test_add_two_numbers_stack_1(self):
        list1 = transform_array_to_list_node(self, [2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers_stack_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([8, 0, 7], actual)

    def test_add_two_numbers_stack_2(self):
        list1 = transform_array_to_list_node(self, [0])
        list2 = transform_array_to_list_node(self, [0])
        res = add_two_numbers_stack_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([0], actual)

    def test_add_two_numbers(self):
        list1 = transform_array_to_list_node(self, [7, 2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([7, 8, 0, 7], actual)

    def test_add_two_numbers_1(self):
        list1 = transform_array_to_list_node(self, [2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([8, 0, 7], actual)

    def test_add_two_numbers_2(self):
        list1 = transform_array_to_list_node(self, [0])
        list2 = transform_array_to_list_node(self, [0])
        res = add_two_numbers_ii(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([0], actual)


if __name__ == '__main__':
    unittest.main()
