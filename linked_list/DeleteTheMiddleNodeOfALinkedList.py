from typing import Optional

from linked_list.DeleteNodeInALinkedList import delete_node
from linked_list.ListNode import ListNode
from linked_list.MiddleOfTheLinkedList import middle_node


# O(n) time || O(1) space
def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    if not head.next.next:
        head.next = None
        return head

    node = middle_node(self, head)
    delete_node(self, node)

    return head
