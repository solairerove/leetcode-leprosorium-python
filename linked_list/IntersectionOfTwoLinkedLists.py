from typing import Optional

from linked_list.ListNode import ListNode


# O(n) time || O(1) space
def get_intersection_node(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    l1, l2 = list1, list2
    while l1 != l2:
        l1 = l1.next if l1 else list2
        l2 = l2.next if l2 else list1

    return l1
