import unittest

from linked_list.ListNode import ListNode
from linked_list.ReverseNodesInKGroup import reverse_k_group


class MyTestCase(unittest.TestCase):
    def test_reverse_k_group(self):
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

        res = reverse_k_group(__name__, head, 2)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([2, 1, 4, 3, 5], arr)  

    def test_reverse_k_group_1(self):
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

        res = reverse_k_group(__name__, head, 3)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([3, 2, 1, 4, 5], arr)  


if __name__ == '__main__':
    unittest.main()
