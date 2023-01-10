from typing import Optional

from linked_list.ListNode import ListNode


def reverse_even_length_groups(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = head, head.next
    cnt, group = 0, 2
    while curr:
        cnt += 1
        if cnt == group:
            if group % 2 == 0:
                curr, prev.next = prev.next, reverse_k_nodes(prev.next, cnt)
            prev = curr
            cnt, group = 0, group + 1

        curr = curr.next

    if cnt % 2 == 0 and prev.next:
        prev.next = reverse_k_nodes(prev.next, cnt)

    return head


def reverse_k_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    prev, curr = None, head
    for i in range(k):
        curr.next, prev, curr = prev, curr, curr.next

    head.next = curr

    return prev
