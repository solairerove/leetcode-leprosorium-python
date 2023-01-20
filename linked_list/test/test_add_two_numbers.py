import unittest

from linked_list.AddTwoNumbers import add_two_numbers
from linked_list.test.utils import transform_array_to_list_node, transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_add_two_numbers(self):
        list1 = transform_array_to_list_node(self, [2, 4, 3])
        list2 = transform_array_to_list_node(self, [5, 6, 4])
        res = add_two_numbers(self, list1, list2)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([7, 0, 8], actual)


if __name__ == '__main__':
    unittest.main()
