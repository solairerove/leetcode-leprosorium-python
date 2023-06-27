from typing import Optional

from linked_list.ListNode import ListNode


# traverse through linked list, relink curr.next to prev, set prev as curr
# in common it looks like changing direction of linking


# O(n) time || O(1) space
def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev
