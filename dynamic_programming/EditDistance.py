from functools import lru_cache


# O(m * n) time || O(m * n) space
def min_distance_top_down(self, s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    @lru_cache(None)
    def dp(i, j):
        if i == m and j == n:
            return 0

        if i == m:
            return n - j

        if j == n:
            return m - i

        if s1[i] == s2[j]:
            return dp(i + 1, j + 1)

        return 1 + min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1))

    return dp(0, 0)


# O(m * n) time || O(m * n) space
def min_distance_bottom_up(self, s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[-1][-1]
