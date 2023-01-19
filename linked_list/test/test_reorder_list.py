import unittest

from linked_list.ListNode import ListNode
from linked_list.ReorderList import reorder_list


class MyTestCase(unittest.TestCase):
    def test_reorder_list(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4
                    )
                )
            )
        )

        reorder_list(__name__, head)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        self.assertEqual([1, 4, 2, 3], arr)  

    def test_reorder_list_2(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4,
                        next=ListNode(5)
                    )
                )
            )
        )

        reorder_list(__name__, head)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        self.assertEqual([1, 5, 2, 4, 3], arr)  


if __name__ == '__main__':
    unittest.main()
