from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or not head.next or (left == 1 and right == 1):
        return head

    sentinel = ListNode(-1)
    prev, curr = sentinel, head
    i = 1
    while curr:
        if i == left:
            prev.next = reverse_k_times(self, curr, right - left + 1)
            break
        prev.next = curr
        prev = prev.next
        curr = curr.next
        i += 1

    return sentinel.next


def reverse_k_times(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    prev, curr = None, head
    for i in range(k):
        curr.next, prev, curr = prev, curr, curr.next

    head.next = curr

    return prev
