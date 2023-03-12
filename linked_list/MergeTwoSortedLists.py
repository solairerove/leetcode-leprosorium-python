from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
        return list1 or list2

    sentinel = ListNode()
    prev, curr1, curr2 = sentinel, list1, list2
    while curr1 and curr2:
        if curr1.val < curr2.val:
            prev.next = curr1
            curr1 = curr1.next
        else:
            prev.next = curr2
            curr2 = curr2.next

        prev = prev.next

    if curr1:
        prev.next = curr1
    elif curr2:
        prev.next = curr2

    return sentinel.next
