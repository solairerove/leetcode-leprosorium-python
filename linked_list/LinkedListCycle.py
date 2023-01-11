from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def has_cycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True

    return False
