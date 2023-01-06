from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev
