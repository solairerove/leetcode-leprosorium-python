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
