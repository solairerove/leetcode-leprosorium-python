from functools import lru_cache
from typing import List


# O(n * w + n) time || O(n * w) space
def knapsack_top_down(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    @lru_cache(None)
    def dp(ith: int, free_space: int) -> int:
        if ith >= n - 1 or free_space < 0:
            return 0

        if weights[ith + 1] > free_space:
            return dp(ith + 1, free_space)

        return max(
            dp(ith + 1, free_space),
            dp(ith + 1, free_space - weights[ith + 1]) + items[ith + 1]
        )

    return dp(-1, capacity)


# O(n * capacity) time || O(n * capacity) space
def knapsack_2d_dp(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for item_id in range(1, n + 1):
        for weight in range(1, capacity + 1):
            curr_weight = weights[item_id - 1]
            curr_max = dp[item_id - 1][weight]

            if curr_weight <= weight:
                dp[item_id][weight] = max(curr_max, dp[item_id - 1][weight - curr_weight] + items[item_id - 1])
            else:
                dp[item_id][weight] = curr_max

    return dp[n][capacity]


# O(n * capacity) time || O(capacity) space
def knapsack_1d_dp(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    dp = [0 for _ in range(capacity + 1)]

    for item_id in range(1, n + 1):
        for weight in range(capacity, 0, -1):
            curr_weight = weights[item_id - 1]

            if curr_weight <= weight:
                dp[weight] = max(dp[weight], dp[weight - curr_weight] + items[item_id - 1])

    return dp[capacity]
