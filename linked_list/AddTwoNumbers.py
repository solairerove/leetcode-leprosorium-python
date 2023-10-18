from typing import Optional

from linked_list.ListNode import ListNode


# calculate in column like in school. use on hold var.

# O(max(n, m)) time || O(1) space
def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode()
    prev = sentinel

    hold = 0
    while l1 or l2:
        curr_sum = 0

        if l1:
            curr_sum, l1 = curr_sum + l1.val, l1.next

        if l2:
            curr_sum, l2 = curr_sum + l2.val, l2.next

        curr_sum += hold

        prev.next, hold = ListNode(curr_sum % 10), curr_sum // 10
        prev = prev.next

    if hold:
        prev.next = ListNode(hold)

    return sentinel.next
