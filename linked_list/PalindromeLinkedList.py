from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def is_palindrome(self, head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    curr1, curr2 = head, prev
    while curr1 and curr2:
        if curr1.val != curr2.val:
            return False

        curr1, curr2 = curr1.next, curr2.next

    return True
