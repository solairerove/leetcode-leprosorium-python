import unittest

from linked_list.ListNode import ListNode
from linked_list.RemoveNodesFromLinkedList import remove_nodes


class MyTestCase(unittest.TestCase):
    def test_remove_nodes_from_linked_list(self):
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

        res = remove_nodes(__name__, head)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([13, 8], arr)  # add assertion here


if __name__ == '__main__':
    unittest.main()
