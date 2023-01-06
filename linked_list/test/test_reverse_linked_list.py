import unittest

from linked_list.ListNode import ListNode
from linked_list.ReverseLinkedList import reverse_list


class MyTestCase(unittest.TestCase):
    def test_reverse_linked_list(self):
        head = ListNode(
            val=5,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=13,
                    next=ListNode(
                        val=3,
                        next=ListNode(
                            val=8
                        )
                    )
                )
            )
        )

        res = reverse_list(__name__, head)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([8, 3, 13, 2, 5], arr)  # add assertion here


if __name__ == '__main__':
    unittest.main()
