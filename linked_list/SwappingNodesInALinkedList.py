from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def swap_nodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    a, b, curr = None, None, head
    while curr:
        k -= 1
        b = None if not b else b.next
        if k == 0:
            a = curr
            b = head
        curr = curr.next
    a.val, b.val = b.val, a.val

    return head
