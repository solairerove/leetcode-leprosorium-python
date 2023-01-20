from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def is_palindrome(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    curr, prev = slow.next, None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    list1, list2 = head, prev
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1, list2 = list1.next, list2.next

    return True
