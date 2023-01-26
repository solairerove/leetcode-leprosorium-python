from typing import Optional

from linked_list.AddTwoNumbers import add_two_numbers
from linked_list.ListNode import ListNode
from linked_list.ReverseLinkedList import reverse_list


# O(n + m) time || O(n + m) space
def add_two_numbers_stack_ii(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 and not l2:
        return None

    if not l1 or not l2:
        return l1 if l1 else l2

    s1, s2 = [], []

    while l1:
        s1.append(l1.val)
        l1 = l1.next

    while l2:
        s2.append(l2.val)
        l2 = l2.next

    head = None
    carry = 0
    while s1 or s2:
        x = s1.pop() if s1 else 0
        y = s2.pop() if s2 else 0
        sm = x + y + carry
        carry = sm // 10

        curr = ListNode(sm % 10)
        curr.next, head = head, curr

    if carry == 1:
        curr = ListNode(1)
        curr.next, head = head, curr

    return head


# O(max(3n, 3m)) time || O(max(n, m) + 1) space
def add_two_numbers_naive_ii(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    reversed_l1, reversed_l2 = reverse_list(self, l1), reverse_list(self, l2)
    two_numbers_sum = add_two_numbers(self, reversed_l1, reversed_l2)
    res = reverse_list(self, two_numbers_sum)

    return res
