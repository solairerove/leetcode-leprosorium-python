from functools import lru_cache
from typing import List


# O(w) time || O(w) space, where w - 365
def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
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
