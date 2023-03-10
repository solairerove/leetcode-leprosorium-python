import random
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    # O(n) time | O(1) space
    def get_random(self) -> int:
        res, scope, curr = 0, 1, self.head
        while curr:
            if random.random() < 1 / scope:
                res = curr.val

            curr, scope = curr.next, scope + 1

        return res
