import unittest

from linked_list.ListNode import ListNode
from linked_list.RemoveNthNodeFromEndOfList import remove_nth_from_end


class MyTestCase(unittest.TestCase):
    def test_remove_nth_from_end(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4,
                        next=ListNode(
                            val=5
                        )
                    )
                )
            )
        )

        remove_nth_from_end(__name__, head, 2)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        self.assertEqual([1, 2, 3, 5], arr)  


if __name__ == '__main__':
    unittest.main()
