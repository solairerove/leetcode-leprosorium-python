from functools import lru_cache


# O(n * m) time || O(n * m) space
def longest_common_subsequence(self, s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # TODO: in range(1, n - 1)
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[-1][-1]


# O(n * m) time || O(n * m) space
def longest_common_subsequence_req(self, s1: str, s2: str) -> int:
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            return dp(i - 1, j - 1) + 1

        return max(dp(i - 1, j), dp(i, j - 1))

    return dp(len(s1) - 1, len(s2) - 1)
