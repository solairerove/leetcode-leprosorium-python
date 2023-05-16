from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    sentinel = ListNode(-1, head)
    prev, curr = sentinel, head
    while curr and curr.next:
        nxt, a, b = curr.next.next, curr, curr.next
        b.next, a.next, prev.next = a, nxt, b
        prev, curr = curr, nxt

    return sentinel.next
