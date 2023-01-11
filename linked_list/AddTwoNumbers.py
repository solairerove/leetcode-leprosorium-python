from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
# 2 4 3 + 5 6 4
def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode()
    prev = sentinel
    curr1, curr2 = l1, l2
    hold = 0
    while curr1 or curr2:
        sum = 0
        if curr1:
            sum += curr1.val
            curr1 = curr1.next

        if curr2:
            sum += curr2.val
            curr2 = curr2.next

        sum += hold

        prev.next = ListNode(sum % 10)
        hold = sum // 10
        prev = prev.next

    if hold != 0:
        prev.next = ListNode(hold)

    return sentinel.next
