from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or not head.next or (left == 1 and right == 1):
        return head

    sentinel = ListNode(-1)
    prev, curr = sentinel, head
    low = high = 1
    while curr:
        if low == left:
            prev.next = reverse_k_times(self, curr, right - left + 1)  #
            break  # change to high += 1 iterations
        prev.next = curr
        prev = prev.next
        curr = curr.next
        low += 1

    return sentinel.next


# 1, 4, 3, 2, 5

def reverse_k_times(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    prev, curr = None, head
    for i in range(k):
        curr.next, prev, curr = prev, curr, curr.next

    head.next = curr

    return prev
