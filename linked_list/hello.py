from typing import Optional

from linked_list.listNode import ListNode


def reverseKNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    curr = head
    prev = None
    for i in range(k):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    head.next = curr

    return prev


class Solution:

    @staticmethod
    def reverseEvenLengthGroups(head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        cnt, group = 0, 2
        while curr:
            cnt += 1
            if cnt == group:
                if group % 2 == 0:
                    curr = prev.next
                    prev.next = reverseKNodes(prev.next, cnt)
                prev = curr
                cnt = 0
                group += 1

            curr = curr.next

        if cnt % 2 == 0 and prev.next:
            prev.next = reverseKNodes(prev.next, cnt)

        return head
