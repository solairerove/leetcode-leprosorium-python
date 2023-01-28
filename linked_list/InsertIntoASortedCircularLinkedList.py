from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(n) space
def insert(self, head: Optional[ListNode], insert_val: int) -> ListNode:
    node = ListNode(insert_val)

    if not head:
        node.next = node
        return node

    prev, curr = head, head.next
    while prev.next != head:
        if prev.val <= node.val <= curr.val:
            break

        if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
            break

        prev, curr = prev.next, curr.next

    node.next = curr
    prev.next = node

    return head
