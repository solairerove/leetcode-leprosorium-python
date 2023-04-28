from functools import lru_cache


# O(m * n) time || O(m * n) space
def is_subsequence_top_down(self, s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)

    @lru_cache(None)
    def dp(i, j):
        if i == m:
            return True

        if j == n:
            return False

        if s1[i] == s2[j]:
            return dp(i + 1, j + 1)

        return dp(i, j + 1)

    return dp(0, 0)
