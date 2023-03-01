from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next

    return head


# O(n) time || O(1) space
def delete_duplicates_dumb(self, head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode()
    prev, curr = sentinel, head
    while curr:
        while curr and curr.next and curr.val == curr.next.val:
            curr = curr.next

        prev.next = curr
        prev = prev.next
        curr = curr.next

    return sentinel.next
