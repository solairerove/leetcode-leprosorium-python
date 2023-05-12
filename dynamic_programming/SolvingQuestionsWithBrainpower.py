from functools import lru_cache
from typing import List


# O(n^2) time || O(n^2) space
def most_points(self, q: List[List[int]]) -> int:
    @lru_cache(None)
    def dp(i: int) -> int:
        return 0 if i >= len(q) else max(dp(i + 1), q[i][0] + dp(i + 1 + q[i][1]))

    return dp(0)
