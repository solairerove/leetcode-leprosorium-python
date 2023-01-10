from typing import Optional

from linked_list.ListNode import ListNode
from linked_list.ReverseLinkedList import reverse_list


def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    reversed_head = reverse_list(self, head)
    curr = reversed_head
    while curr and curr.next:
        if curr.val > curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return reverse_list(self, reversed_head)
