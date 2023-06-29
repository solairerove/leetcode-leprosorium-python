from typing import Optional

from linked_list.ListNode import ListNode


# traverse linked list using two pointers. the first is current, the second is offset to n.
# when traverse is done, the second pointer will be prev to deleted.

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
