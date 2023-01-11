import unittest

from linked_list.LinkedListCycle import has_cycle
from linked_list.ListNode import ListNode


class MyTestCase(unittest.TestCase):
    def test_has_cycle(self):
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        res = has_cycle(__name__, node1)

        self.assertEqual(True, res)  # add assertion here

    def test_has_cycle_1(self):
        node1 = ListNode(1)
        node2 = ListNode(2)

        node1.next = node2
        node2.next = node1

        res = has_cycle(__name__, node1)

        self.assertEqual(True, res)  # add assertion here

    def test_has_cycle_2(self):
        node1 = ListNode(1)

        res = has_cycle(__name__, node1)

        self.assertEqual(False, res)  # add assertion here

    def test_has_cycle_6(self):
        node1 = ListNode(1)
        node2 = ListNode(2)

        node1.next = node2

        res = has_cycle(__name__, node1)

        self.assertEqual(False, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
