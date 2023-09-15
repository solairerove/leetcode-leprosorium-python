from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(-1)
    prev = sentinel
    curr1, curr2 = list1, list2
    while curr1 and curr2:
        if curr1.val <= curr2.val:
            prev.next, curr1 = curr1, curr1.next
        else:
            prev.next, curr2 = curr2, curr2.next

        prev = prev.next

    prev.next = curr1 or curr2

    return sentinel.next
