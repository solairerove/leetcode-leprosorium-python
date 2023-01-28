import unittest

from linked_list.InsertIntoASortedCircularLinkedList import insert
from linked_list.ListNode import ListNode


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1 = ListNode(1)

        node3.next = node4
        node4.next = node1
        node1.next = node3
        res = insert(self, node3, 2)
        self.assertEqual(3, res.val)
        self.assertEqual(4, res.next.val)
        self.assertEqual(1, res.next.next.val)
        self.assertEqual(2, res.next.next.next.val)
        self.assertEqual(res, res.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
