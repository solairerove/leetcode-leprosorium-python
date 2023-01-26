from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd_head, even_head = head, head.next
    odd, even = odd_head, even_head
    while odd.next and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        even, odd = even.next, odd.next

    odd.next = even_head

    return odd_head
