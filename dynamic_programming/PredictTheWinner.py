from functools import lru_cache
from typing import List


# O(n ^ 2) time || O(n) space
def predict_the_winner(self, nums: List[int]) -> bool:
    @lru_cache
    def dp(s, e):
        if s == e:
            return nums[e]

        return max(
            nums[e] - dp(s, e - 1),
            nums[s] - dp(s + 1, e)
        )

    return dp(0, len(nums) - 1) >= 0
