from functools import lru_cache


# O(n * m) time || O(n * m) space
def longest_common_subsequence_top_down(self, s1: str, s2: str) -> int:
    @lru_cache(None)
    def dp(i, j):
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            return 1 + dp(i - 1, j - 1)

        return max(dp(i, j - 1), dp(i - 1, j))

    return dp(len(s1) - 1, len(s2) - 1)


# O(n * m) time || O(n * m) space
def longest_common_subsequence_bottom_up(self, s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1]
