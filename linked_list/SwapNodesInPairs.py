from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    if not head.next:
        return head

    sentinel = ListNode(-1, head)
    prev, curr = sentinel, head
    i = 0
    while curr:
        if i % 2 == 0:
            prev.next, prev = reverse_two_nodes(self, prev.next), curr
        else:
            i += 1
        curr = curr.next

    return sentinel.next


def reverse_two_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    i = 0
    while curr and i < 2:
        curr.next, prev, curr = prev, curr, curr.next
        i += 1

    head.next = curr

    return prev
