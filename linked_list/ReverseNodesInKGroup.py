from typing import Optional

from linked_list.ListNode import ListNode


# O(2n) time || O(1) space
def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    sentinel = ListNode(-1, head)
    group_prev = sentinel
    while True:
        kth = find_kth(self, group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            curr.next, prev, curr = prev, curr, curr.next

        group_prev.next, group_prev = kth, group_prev.next

    return sentinel.next


def find_kth(self, curr, k) -> Optional[ListNode]:
    while curr and k > 0:
        k -= 1
        curr = curr.next

    return curr
