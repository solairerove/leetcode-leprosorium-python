import random
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    # O(n) time | O(1) space
    def get_random(self) -> int:
        scope = 1
        chosen_value = 0

        curr = self.head
        while curr:
            if random.random() < 1 / scope:
                chosen_value = curr.val
            curr, scope = curr.next, scope + 1

        return chosen_value
