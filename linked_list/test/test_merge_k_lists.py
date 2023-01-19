import unittest

from linked_list.ListNode import ListNode
from linked_list.MergeKSortedLists import merge_k_lists


class MyTestCase(unittest.TestCase):
    def test_merge_k_lists(self):
        node1 = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=5)))
        node2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
        node3 = ListNode(val=2, next=ListNode(val=6))

        res = merge_k_lists(__name__, [node1, node2, node3])
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], arr)  


if __name__ == '__main__':
    unittest.main()
