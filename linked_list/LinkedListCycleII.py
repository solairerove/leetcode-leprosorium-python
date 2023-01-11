from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    has_cycle = False
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    slow = head
    while slow != fast:
        slow, fast = slow.next, fast.next

    return slow
