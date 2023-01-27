from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    sentinel = ListNode()
    prev, curr = sentinel, head
    while curr:
        if curr and curr.next and curr.val == curr.next.val:
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next
        else:
            prev.next = curr
            prev = prev.next
        curr = curr.next

    prev.next = None

    return sentinel.next
