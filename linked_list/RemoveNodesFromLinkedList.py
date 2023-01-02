from typing import Optional

from linked_list.ListNode import ListNode


def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    reversed_head = reverse_linked_list(self, head)
    curr = reversed_head
    while curr and curr.next:
        if curr.val > curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return reverse_linked_list(self, reversed_head)


def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev
