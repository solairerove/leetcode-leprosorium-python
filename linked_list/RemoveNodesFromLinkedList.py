from typing import Optional

from linked_list.listNode import ListNode


class Sou:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = reverseLinkedList(self, head)
        curr = reversedHead
        while curr and curr.next:
            if curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return reverseLinkedList(self, reversedHead)


def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev
