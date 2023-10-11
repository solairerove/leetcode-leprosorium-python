from functools import lru_cache
from typing import List


# O(n * w + n) time || O(n * w) space
def knapsack_top_down(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    @lru_cache(None)
    def dp(i, free_space):
        if i < 1 or free_space < 0:
            return 0

        if weights[i - 1] > free_space:
            return dp(i - 1, free_space)

        return max(
            dp(i - 1, free_space),
            dp(i - 1, free_space - weights[i - 1]) + items[i - 1]
        )

    return dp(n, capacity)


# O(n * capacity) time || O(n * capacity) space
def knapsack_bottom_up(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], items[i - 1] + dp[i - 1][j - weights[i - 1]])

    return dp[-1][-1]


# O(n * capacity) time || O(capacity) space
def knapsack_1d_dp(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    dp = [0 for _ in range(capacity + 1)]

    for item_id in range(1, n + 1):
        for weight in range(capacity, 0, -1):
            curr_weight = weights[item_id - 1]

            if curr_weight <= weight:
                dp[weight] = max(dp[weight], dp[weight - curr_weight] + items[item_id - 1])

    return dp[capacity]
