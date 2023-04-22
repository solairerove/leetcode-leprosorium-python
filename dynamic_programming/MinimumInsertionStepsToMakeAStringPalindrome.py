from functools import lru_cache


# O(n^2) time || O(n^2) space
def min_insertions_top_down(self, s: str) -> int:
    @lru_cache(None)
    def dp(low, high):
        if low >= high:
            return 0

        if s[low] == s[high]:
            return dp(low + 1, high - 1)

        return 1 + min(dp(low, high - 1), dp(low + 1, high))

    return dp(0, len(s) - 1)


# O(n^2) time || O(n^2) space
def min_insertions_bottom_up(self, s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i + 1][j])

    return dp[0][n - 1]


# O(n^2) time || O(n) space
def min_insertions(self, s: str) -> int:
    n = len(s)
    dp, dp_prev = [0] * n, [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[j] = dp_prev[j - 1]
            else:
                dp[j] = 1 + min(dp[j - 1], dp_prev[j])
        dp, dp_prev = dp_prev, dp

    return dp_prev[n - 1]
