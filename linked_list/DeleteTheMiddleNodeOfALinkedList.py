from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None

    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next

    prev.next = prev.next.next

    return head
