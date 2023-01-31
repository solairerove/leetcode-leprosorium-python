import unittest

from linked_list.MaximumTwinSumOfALinkedList import pair_sum
from linked_list.test.utils import transform_array_to_list_node


class MyTestCase(unittest.TestCase):
    def test_pair_sum(self):
        head = transform_array_to_list_node(self, [5, 4, 2, 1])
        actual = pair_sum(self, head)

        self.assertEqual(6, actual)

    def test_pair_sum_1(self):
        head = transform_array_to_list_node(self, [4, 2, 2, 3])
        actual = pair_sum(self, head)

        self.assertEqual(7, actual)

    def test_pair_sum_2(self):
        head = transform_array_to_list_node(self, [1, 100000])
        actual = pair_sum(self, head)

        self.assertEqual(100001, actual)


if __name__ == '__main__':
    unittest.main()
