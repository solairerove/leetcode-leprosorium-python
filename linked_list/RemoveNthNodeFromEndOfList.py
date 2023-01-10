from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    sentinel = ListNode(-1, head)
    prev, curr = sentinel, head
    while curr:
        n = n - 1
        if n < 0:
            prev = prev.next
        curr = curr.next

    if prev.next:
        prev.next = prev.next.next

    return sentinel.next
