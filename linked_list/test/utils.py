from typing import Optional

from linked_list.ListNode import ListNode


def transform_array_to_list_node(self, arr) -> Optional[ListNode]:
    head = ListNode(arr[0])
    prev = head
    for i in range(1, len(arr)):
        prev.next = ListNode(arr[i])
        prev = prev.next

    return head


def transform_list_node_to_array(self, head: Optional[ListNode]) -> []:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    return arr
