from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2

    if not list2:
        return list1

    sentinel = ListNode()
    prev = sentinel
    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next

        prev = prev.next

    prev.next = list1 if list1 else list2

    return sentinel.next
