from typing import Optional

from linked_list.ListNode import ChildListNode


# O(n) time || O(1) space
def flatten(self, head: Optional[ChildListNode]) -> Optional[ChildListNode]:
    if not head or (not head.next and not head.prev and not head.child):
        return head

    sentinel = ChildListNode(-1, None, head, None)
    prev = sentinel

    stack = [head]
    while stack:
        curr = stack.pop()

        prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)

        if curr.child:
            stack.append(curr.child)
            curr.child = None

        prev = curr

    sentinel.next.prev = None

    return sentinel.next
