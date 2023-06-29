from typing import Optional

from linked_list.ListNode import RandomListNode


# create copy node next to origin, relink random node, create new linked list using copies

# O(3n) time || O(1) space
def copy_random_list(self, head: 'Optional[RandomListNode]') -> 'Optional[RandomListNode]':
    curr = head
    while curr:
        curr.next, curr = RandomListNode(curr.val, curr.next), curr.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    sentinel = RandomListNode(-1)
    prev, curr = sentinel, head
    while curr:
        prev.next = curr.next
        prev, curr = prev.next, curr.next.next

    return sentinel.next
