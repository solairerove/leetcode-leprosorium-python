import unittest

from linked_list.FlattenAMultilevelDoublyLinkedList import flatten
from linked_list.ListNode import ChildListNode
from linked_list.test.utils import transform_list_node_to_array


class MyTestCase(unittest.TestCase):
    def test_flatten(self):
        node1 = ChildListNode(val=1, prev=None, next=None, child=None)
        node2 = ChildListNode(val=2, prev=None, next=None, child=None)
        node3 = ChildListNode(val=3, prev=None, next=None, child=None)
        node4 = ChildListNode(val=4, prev=None, next=None, child=None)
        node5 = ChildListNode(val=5, prev=None, next=None, child=None)
        node6 = ChildListNode(val=6, prev=None, next=None, child=None)
        node7 = ChildListNode(val=7, prev=None, next=None, child=None)
        node8 = ChildListNode(val=8, prev=None, next=None, child=None)
        node9 = ChildListNode(val=9, prev=None, next=None, child=None)
        node10 = ChildListNode(val=10, prev=None, next=None, child=None)
        node11 = ChildListNode(val=11, prev=None, next=None, child=None)
        node12 = ChildListNode(val=12, prev=None, next=None, child=None)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        node7.next = node8
        node8.next = node9
        node9.next = node10

        node11.next = node12

        node2.prev = node1
        node3.prev = node2
        node4.prev = node3
        node5.prev = node4
        node6.prev = node5

        node8.prev = node7
        node9.prev = node8
        node10.prev = node9

        node12.prev = node11

        node3.child = node7
        node8.child = node11

        res = flatten(self, node1)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6], actual)

    def test_flatten_1(self):
        node1 = ChildListNode(val=1, prev=None, next=None, child=None)
        node2 = ChildListNode(val=2, prev=None, next=None, child=None)
        node3 = ChildListNode(val=3, prev=None, next=None, child=None)

        node1.next = node2

        node2.prev = node1

        node1.child = node3

        res = flatten(self, node1)
        actual = transform_list_node_to_array(self, res)

        self.assertEqual([1, 3, 2], actual)

    def test_flatten_2(self):
        self.assertEqual(None, flatten(self, None))


if __name__ == '__main__':
    unittest.main()
