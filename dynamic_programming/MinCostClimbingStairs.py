from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def min_cost_climbing_stairs(self, cost: List[int]) -> int:
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])


# O(n) time || O(n) space
def min_cost_climbing_stairs_rec(self, cost: List[int]) -> int:
    @lru_cache(None)
    def dp(i) -> int:
        if i >= len(cost):
            return 0

        return cost[i] + min(dp(i + 1), dp(i + 2))

    return min(dp(0), dp(1))
