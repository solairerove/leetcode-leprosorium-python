from functools import lru_cache


# O(m * n) time || O(m * n) space
def unique_paths(self, m: int, n: int) -> int:
    @lru_cache(None)
    def dp(i, j):
        if i < 1 or j < 1:
            return 0

        if i == 1 and j == 1:
            return 1

        return dp(i - 1, j) + dp(i, j - 1)

    return dp(m, n)
