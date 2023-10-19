from typing import List, Optional

from linked_list.ListNode import ListNode


# need to implement merge_two_lists from problem 21
# use interval to increase performance(like merge sort)

# O(n * log(k)) time | O(1) space
# n - is total number of nodes
# k - is number of linked lists
def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    offset = 1
    while offset < len(lists):
        for i in range(0, len(lists) - offset, offset * 2):
            lists[i] = merge(self, lists[i], lists[i + offset])
        offset *= 2

    return lists[0]


# 21. Merge Two Sorted Lists
def merge(self, l1, l2):
    sentinel = ListNode()
    prev = sentinel
    curr1, curr2 = l1, l2
    while curr1 and curr2:
        if curr1.val < curr2.val:
            prev.next, curr1 = curr1, curr1.next
        else:
            prev.next, curr2 = curr2, curr2.next

        prev = prev.next

    prev.next = curr1 or curr2

    return sentinel.next
