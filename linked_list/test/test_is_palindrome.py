import unittest

from linked_list.ListNode import ListNode
from linked_list.PalindromeLinkedList import is_palindrome


class MyTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=2,
                    next=ListNode(
                        val=1
                    )
                )
            )
        )

        self.assertEqual(True, is_palindrome(self, head))

    def test_is_palindrome_1(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
            )
        )

        self.assertEqual(False, is_palindrome(self, head))


if __name__ == '__main__':
    unittest.main()
