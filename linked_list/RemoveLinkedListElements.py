from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    sentinel = ListNode()
    prev, curr = sentinel, head
    while curr:
        if curr.val != val:
            prev.next = curr
            prev = prev.next

        curr = curr.next

    prev.next = None

    return sentinel.next
