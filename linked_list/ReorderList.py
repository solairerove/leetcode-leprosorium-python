from typing import Optional

from linked_list.ListNode import ListNode


# find middle node, reverse the second part, merge with reordering

# O(n) time || O(1) space
def reorder_list(self, head: Optional[ListNode]) -> None:
    if not head.next:
        return None

    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first, second = head, prev
    while first and second:
        first.next, first = second, first.next
        second.next, second = first, second.next
