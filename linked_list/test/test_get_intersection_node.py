import unittest

from linked_list.IntersectionOfTwoLinkedLists import get_intersection_node
from linked_list.ListNode import ListNode


class MyTestCase(unittest.TestCase):
    def test_get_intersection_node(self):
        node1 = ListNode(4)
        node2 = ListNode(1)
        node3 = ListNode(8)
        node4 = ListNode(4)
        node5 = ListNode(5)

        node6 = ListNode(5)
        node7 = ListNode(6)
        node8 = ListNode(1)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node6.next = node7
        node7.next = node8
        node8.next = node3

        res = get_intersection_node(self, node1, node6)

        self.assertEqual(8, res.val)

    def test_get_intersection_node_1(self):
        node1 = ListNode(1)
        node2 = ListNode(9)
        node3 = ListNode(1)
        node4 = ListNode(2)
        node5 = ListNode(4)

        node6 = ListNode(3)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node6.next = node4

        res = get_intersection_node(self, node1, node6)

        self.assertEqual(2, res.val)

    def test_get_intersection_node_2(self):
        node1 = ListNode(2)
        node2 = ListNode(6)
        node3 = ListNode(4)

        node6 = ListNode(1)
        node7 = ListNode(5)

        node1.next = node2
        node2.next = node3

        node6.next = node7

        res = get_intersection_node(self, node1, node6)

        self.assertEqual(None, res)


if __name__ == '__main__':
    unittest.main()
