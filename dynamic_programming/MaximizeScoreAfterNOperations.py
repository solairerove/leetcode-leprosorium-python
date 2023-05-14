import math
from functools import lru_cache
from typing import List


# O(2^m * m^2) time || O(2^m) space
def max_score(self, nums: List[int]) -> int:
    @lru_cache(None)
    def gcd(x, y):
        return math.gcd(x, y)

    @lru_cache(None)
    def dp(op, mask):
        if op == n + 1:
            return 0

        ans = 0
        for i in range(m):
            if (mask >> i) & 1:
                continue

            for j in range(i + 1, m):
                if (mask >> j) & 1:
                    continue

                new_mask = (1 << i) | (1 << j) | mask
                score = op * gcd(nums[i], nums[j]) + dp(op + 1, new_mask)
                ans = max(ans, score)

        return ans

    m = len(nums)
    n = m // 2

    return dp(1, 0)
