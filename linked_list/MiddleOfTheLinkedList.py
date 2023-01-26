from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    return slow
