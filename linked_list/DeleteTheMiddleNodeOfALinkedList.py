from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    if not slow.next:
        head.next = None
        return head

    slow.val = slow.next.val
    slow.next = slow.next.next

    return head
