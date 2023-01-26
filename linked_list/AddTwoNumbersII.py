from typing import Optional

from linked_list.AddTwoNumbers import add_two_numbers
from linked_list.ListNode import ListNode
from linked_list.ReverseLinkedList import reverse_list


# O(n + m) time || O(1) and O(max(n,m)) for res space
def add_two_numbers_ii(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    n1 = n2 = 0
    curr1, curr2 = l1, l2

    while curr1:
        curr1, n1 = curr1.next, n1 + 1

    while curr2:
        curr2, n2 = curr2.next, n2 + 1

    curr1, curr2 = l1, l2
    head = None
    while n1 > 0 and n2 > 0:
        val = 0
        if n1 >= n2:
            val += curr1.val
            curr1, n1 = curr1.next, n1 - 1

        if n1 < n2:
            val += curr2.val
            curr2, n2 = curr2.next, n2 - 1

        curr = ListNode(val)
        curr.next = head
        head = curr

    curr1 = head
    head = None
    carry = 0
    while curr1:
        sm = curr1.val + carry
        val = sm % 10
        carry = sm // 10

        curr = ListNode(val)
        curr.next = head
        head = curr

        curr1 = curr1.next

    if carry != 0:
        curr = ListNode(carry)
        curr.next = head
        head = curr

    return head


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
    while s1 or s2 or carry != 0:
        x = s1.pop() if s1 else 0
        y = s2.pop() if s2 else 0
        sm = x + y + carry
        carry = sm // 10

        curr = ListNode(sm % 10)
        curr.next, head = head, curr

    return head


# O(max(3n, 3m)) time || O(max(n, m) + 1) space
def add_two_numbers_naive_ii(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    reversed_l1, reversed_l2 = reverse_list(self, l1), reverse_list(self, l2)
    two_numbers_sum = add_two_numbers(self, reversed_l1, reversed_l2)
    res = reverse_list(self, two_numbers_sum)

    return res
