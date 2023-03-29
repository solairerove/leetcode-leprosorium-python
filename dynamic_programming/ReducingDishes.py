from functools import lru_cache
from typing import List


# O(n^2) time || O(n^2) space
def max_satisfaction(self, satisfaction: List[int]) -> int:
    satisfaction.sort()

    @lru_cache(None)
    def dp(i, t):
        if i >= len(satisfaction):
            return 0

        return max(dp(i + 1, t), satisfaction[i] * t + dp(i + 1, t + 1))

    return dp(0, 1)


# O(n * log(n)) time || O(1) space
def max_satisfaction_greedy(self, satisfaction: List[int]) -> int:
    satisfaction.sort()

    res = total = 0
    while satisfaction and satisfaction[-1] + total > 0:
        total += satisfaction.pop()
        res += total

    return res
