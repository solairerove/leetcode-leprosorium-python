import unittest

from linked_list.ListNode import ListNode
from linked_list.MergeTwoSortedLists import merge_two_lists


class MyTestCase(unittest.TestCase):
    def test_merge_two_lists(self):
        list1 = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=4
                )
            )
        )

        list2 = ListNode(
            val=1,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4
                )
            )
        )

        res = merge_two_lists(__name__, list1, list2)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([1, 1, 2, 3, 4, 4], arr)  


if __name__ == '__main__':
    unittest.main()
