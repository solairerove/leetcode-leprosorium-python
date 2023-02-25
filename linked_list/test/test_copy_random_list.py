import unittest

from linked_list.CopyListWithRandomPointer import copy_random_list
from linked_list.ListNode import RandomListNode


class MyTestCase(unittest.TestCase):
    def test_copy_random_list(self):
        node1 = RandomListNode(7)
        node2 = RandomListNode(13)
        node3 = RandomListNode(11)
        node4 = RandomListNode(10)
        node5 = RandomListNode(1)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node2.random = node1
        node3.random = node5
        node4.random = node3
        node5.random = node1

        res = copy_random_list(__name__, node1)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next

        self.assertEqual([7, 13, 11, 10, 1], arr)  


if __name__ == '__main__':
    unittest.main()
