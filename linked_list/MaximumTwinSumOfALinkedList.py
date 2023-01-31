from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time | O(1) space
def pair_sum(self, head: Optional[ListNode]) -> int:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    sm = 0
    first, second = head, prev
    while second:
        sm = max(sm, first.val + second.val)
        first, second = first.next, second.next

    return sm
