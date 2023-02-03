from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def min_cost_climbing_stairs(self, cost: List[int]) -> int:
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])


# O(n) time || O(n) space
def min_cost_climbing_stairs_rec_bottom_up(self, cost: List[int]) -> int:
    @lru_cache(None)
    def helper(s) -> int:
        if s < 2:
            return 0

        return min(cost[s - 1] + helper(s - 1), cost[s - 2] + helper(s - 2))

    return helper(len(cost))


# O(n) time || O(n) space
def min_cost_climbing_stairs_rec_top_down(self, cost: List[int]) -> int:
    @lru_cache(None)
    def helper(ith) -> int:
        if ith >= len(cost) - 2:
            return 0

        return min(cost[ith + 1] + helper(ith + 1), cost[ith + 2] + helper(ith + 2))

    return helper(-1)
