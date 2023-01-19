import unittest

from linked_list.ListNode import ListNode
from linked_list.ReverseNodesInEvenLengthGroups import reverse_even_length_groups


class MyTestCase(unittest.TestCase):
    def test_reverse_even_length_groups(self):
        head = ListNode(
            val=5,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=6,
                    next=ListNode(
                        val=3,
                        next=ListNode(
                            val=9,
                            next=ListNode(
                                val=1,
                                next=ListNode(
                                    val=7,
                                    next=ListNode(
                                        val=3,
                                        next=ListNode(
                                            val=8,
                                            next=ListNode(
                                                val=4
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )

        res = reverse_even_length_groups(head)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next
        self.assertEqual([5, 6, 2, 3, 9, 1, 4, 8, 3, 7], arr)  


if __name__ == '__main__':
    unittest.main()
