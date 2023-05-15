from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def swap_nodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    start, end, curr = None, None, head
    while curr:
        k -= 1
        end = None if not end else end.next
        if k == 0:
            start, end = curr, head

        curr = curr.next

    start.val, end.val = end.val, start.val

    return head
