import unittest

from linked_list.PalindromeLinkedList import is_palindrome
from linked_list.test.utils import transform_array_to_list_node


class MyTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        head = transform_array_to_list_node(self, [1, 2, 2, 1])
        actual = is_palindrome(self, head)

        self.assertEqual(True, actual)

    def test_is_palindrome_1(self):
        head = transform_array_to_list_node(self, [1, 2])
        actual = is_palindrome(self, head)

        self.assertEqual(False, actual)


if __name__ == '__main__':
    unittest.main()
