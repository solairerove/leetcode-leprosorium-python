from typing import Optional

from linked_list.AddTwoNumbers import add_two_numbers
from linked_list.ListNode import ListNode
from linked_list.ReverseLinkedList import reverse_list


# O(max(3n, 3m)) time || O(max(n, m) + 1) space
def add_two_numbers_naive_ii(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    reversed_l1, reversed_l2 = reverse_list(self, l1), reverse_list(self, l2)
    two_numbers_sum = add_two_numbers(self, reversed_l1, reversed_l2)
    res = reverse_list(self, two_numbers_sum)

    return res
