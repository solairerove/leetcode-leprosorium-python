from functools import lru_cache
from typing import List


# O(w) time || O(w) space, where w - 365
def min_cost_tickets_all_days(self, days: List[int], costs: List[int]) -> int:
    day_set = set(days)
    durations = [1, 7, 30]

    @lru_cache(365)
    def dp(i):
        if i > 365:
            return 0
        elif i in day_set:
            return min(dp(i + d) + c for c, d in zip(costs, durations))
        else:
            return dp(i + 1)

    return dp(1)


# O(n) time || O(n) space, where n - unique days
def min_cost_tickets_window(self, days: List[int], costs: List[int]) -> int:
    n = len(days)
    durations = [1, 7, 30]

    @lru_cache(None)
    def dp(i):
        if i >= n:
            return 0

        res = float('inf')
        j = i
        for c, d in zip(costs, durations):
            while j < n and days[j] < days[i] + d:
                j += 1
            res = min(res, dp(j) + c)

        return res

    return dp(0)


# O(n) time || O(n) space, where n - unique days
def min_cost_tickets_bottom_up(self, days: List[int], costs: List[int]) -> int:
    dp = [0] * (days[-1] + 1)
    for i in range(1, len(dp)):
        if i in days:
            dp[i] = min(
                dp[max(i - 1, 0)] + costs[0],
                dp[max(i - 7, 0)] + costs[1],
                dp[max(i - 30, 0)] + costs[2]
            )
        else:
            dp[i] = dp[i - 1]

    return dp[-1]
