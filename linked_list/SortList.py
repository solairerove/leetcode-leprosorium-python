from typing import Optional

from linked_list.ListNode import ListNode
from linked_list.MergeTwoSortedLists import merge_two_lists


# O(n * log(n)) time || O(n * log(n)) space
def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    mid = get_mid(self, head)
    left, right = sort_list(self, head), sort_list(self, mid)

    return merge_two_lists(self, left, right)


def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
    mid_prev = None
    while head and head.next:
        if mid_prev:
            mid_prev = mid_prev.next
        else:
            mid_prev = head
        head = head.next.next

    mid = mid_prev.next
    mid_prev.next = None

    return mid
