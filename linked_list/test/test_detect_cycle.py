import unittest

from linked_list.LinkedListCycleII import detect_cycle
from linked_list.ListNode import ListNode


class MyTestCase(unittest.TestCase):
    def test_detect_cycle(self):
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        res = detect_cycle(__name__, node1)

        self.assertEqual(2, res.val)  # add assertion here

    def test_detect_cycle_1(self):
        node1 = ListNode(1)
        node2 = ListNode(2)

        node1.next = node2
        node2.next = node1

        res = detect_cycle(__name__, node1)

        self.assertEqual(1, res.val)  # add assertion here

    def test_detect_cycle_2(self):
        node1 = ListNode(1)

        res = detect_cycle(__name__, node1)

        self.assertEqual(None, res)  # add assertion here

    def test_detect_cycle_6(self):
        node1 = ListNode(1)
        node2 = ListNode(2)

        node1.next = node2

        res = detect_cycle(__name__, node1)

        self.assertEqual(None, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
