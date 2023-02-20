import math
from functools import lru_cache
from typing import List


# O(l * m * n) time || O(m * n) space
def find_max_form(self, strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    counter = [[s.count("0"), s.count("1")] for s in strs]
    for zeros, ones in counter:
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

    return dp[-1][-1]


# O(l * m * n) time || O(l * m * n) space
def find_max_form_rec(self, strs: List[str], m: int, n: int) -> int:
    counter = [[s.count("0"), s.count("1")] for s in strs]

    @lru_cache(None)
    def dp(i, j, idx):
        if i < 0 or j < 0:
            return -math.inf

        if idx == len(strs):
            return 0

        return max(dp(i, j, idx + 1), 1 + dp(i - counter[idx][0], j - counter[idx][1], idx + 1))

    return dp(m, n, 0)
