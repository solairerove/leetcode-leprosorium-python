from typing import Optional

from linked_list.ListNode import ListNode


# O(n^2) time || O(1) space
def insertion_sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    sentinel = ListNode()
    curr = head
    while curr:
        prev = sentinel
        while prev.next and curr.val >= prev.next.val:
            prev = prev.next

        curr.next, prev.next, curr = prev.next, curr, curr.next

    return sentinel.next
