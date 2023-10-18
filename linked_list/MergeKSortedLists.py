from typing import List, Optional

from linked_list.ListNode import ListNode


# i like the first solution because i can write it)
# need to implement merge_two_lists from problem 21
# use interval to increase performance(like merge sort)

# O(Nlog(k)) time | O(1) space
# N - is total number of nodes
# k - is number of linked lists
def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    interval = 1
    while interval < len(lists):
        i = 0
        while i + interval < len(lists):
            lists[i] = merge(self, lists[i], lists[i + interval])
            i += interval * 2
        interval *= 2

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
