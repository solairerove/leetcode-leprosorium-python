from functools import lru_cache
from typing import List


# O(n * t) time || O(n * t) space
def combination_sum_4_top_down(self, nums: List[int], target: int) -> int:
    @lru_cache(None)
    def dp(remain):
        if remain == 0:
            return 1

        res = 0
        for num in nums:
            if remain - num >= 0:
                res += dp(remain - num)

        return res

    return dp(target)
