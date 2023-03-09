from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    slow = fast = head
    have_cycle = False
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            have_cycle = True
            break

    if have_cycle:
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next

        return slow

    return None
