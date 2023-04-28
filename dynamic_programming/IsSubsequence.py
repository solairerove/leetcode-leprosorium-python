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


# O(min(m, n)) time || O(1) space
def is_subsequence(self, s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    i, j = 0, 0
    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1

        j += 1

    return i == m if 1 else 0


# O(m + n) time || O(1) space
def is_subsequence_liner(self, s1: str, s2: str) -> bool:
    s2 = iter(s2)

    return all(c in s2 for c in s1)
