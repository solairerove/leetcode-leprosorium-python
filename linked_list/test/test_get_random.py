import unittest

from linked_list.LinkedListRandomNode import Solution
from linked_list.test.utils import transform_array_to_list_node


class MyTestCase(unittest.TestCase):
    def test_get_random(self):
        solution = Solution(transform_array_to_list_node(self, [1, 2, 3]))
        self.assertEqual(True, solution.get_random() in [1, 2, 3])
        self.assertEqual(True, solution.get_random() in [1, 2, 3])
        self.assertEqual(True, solution.get_random() in [1, 2, 3])
        self.assertEqual(True, solution.get_random() in [1, 2, 3])
        self.assertEqual(True, solution.get_random() in [1, 2, 3])
        self.assertEqual(True, solution.get_random() in [1, 2, 3])
        self.assertEqual(True, solution.get_random() in [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
