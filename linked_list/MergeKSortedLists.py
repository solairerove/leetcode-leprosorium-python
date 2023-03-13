import heapq
from typing import List, Optional

from linked_list.ListNode import ListNode
from linked_list.MergeTwoSortedLists import merge_two_lists


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
            lists[i] = merge_two_lists(self, lists[i], lists[i + interval])
            i += interval * 2
        interval *= 2

    return lists[0]


# O(Nlog(k)) time | O(k) space
# N - is total number of nodes
# k - is number of linked lists
def merge_k_lists_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    sentinel = prev = ListNode(0)
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    while heap:
        val, i = heapq.heappop(heap)
        prev.next = ListNode(val)
        prev = prev.next
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return sentinel.next
