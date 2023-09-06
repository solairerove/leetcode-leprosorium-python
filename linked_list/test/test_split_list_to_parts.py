import unittest

from linked_list.SplitLinkedListInParts import split_list_to_parts
from linked_list.test.utils import transform_array_to_list_node


class MyTestCase(unittest.TestCase):
    def test_split_list_to_parts(self):
        head = transform_array_to_list_node(self, [1, 2, 3])
        res = split_list_to_parts(self, head, 5)
        self.assertEqual(1, res[0].val)
        self.assertEqual(2, res[1].val)


if __name__ == '__main__':
    unittest.main()
