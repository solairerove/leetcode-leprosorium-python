from functools import lru_cache
from typing import List


# O(2^n) time || O(n) space
def knapsack_recursion(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    @lru_cache(None)
    def helper(ith: int, free_space: int) -> int:
        if ith >= n - 1 or free_space < 0:
            return 0

        if weights[ith + 1] > free_space:
            return helper(ith + 1, free_space)
        else:
            return max(
                helper(ith + 1, free_space),
                helper(ith + 1, free_space - weights[ith + 1]) + items[ith + 1]
            )

    return helper(-1, capacity)
