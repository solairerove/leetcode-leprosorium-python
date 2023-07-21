from typing import Optional

from linked_list.ListNode import ListNode


# as usual some algo that we should know to solve this shit.

# O(n) time || O(1) space
def has_cycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            return True

    return False
