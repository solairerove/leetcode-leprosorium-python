from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(-1, head)
    prev, curr = sentinel, head

    while curr and curr.next:
        nxt_pair, sec = curr.next.next, curr.next
        sec.next, curr.next, prev.next = curr, nxt_pair, sec
        prev, curr = curr, nxt_pair

    return sentinel.next
