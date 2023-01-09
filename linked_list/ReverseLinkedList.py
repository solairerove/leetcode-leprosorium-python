from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    return prev
