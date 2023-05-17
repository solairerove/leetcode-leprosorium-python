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

    max_sum = 0
    a, b = head, prev
    while b:
        max_sum = max(max_sum, a.val + b.val)
        a, b = a.next, b.next

    return max_sum
