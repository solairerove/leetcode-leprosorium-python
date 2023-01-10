from typing import Optional

from linked_list.ListNode import Node


# O(3n) time || O(1) space
def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
    curr = head
    while curr:
        curr.next, curr = Node(curr.val, curr.next), curr.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    copy_head = Node(-1)
    copy = copy_head
    while curr:
        copy.next = curr.next
        copy, curr = copy.next, curr.next.next

    return copy_head.next
