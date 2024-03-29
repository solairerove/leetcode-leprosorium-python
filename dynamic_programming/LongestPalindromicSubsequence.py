from functools import lru_cache


# O(n^2) time || O(n^2) space, TLE
def longest_palindrome_subseq_top_down(self, s: str) -> int:
    @lru_cache(None)
    def dp(i, j):
        if i > j:
            return 0

        if i == j:
            return 1

        if s[i] == s[j]:
            return dp(i + 1, j - 1) + 2

        return max(dp(i, j - 1), dp(i + 1, j))

    return dp(0, len(s) - 1)


# O(n^2) time || O(n^2) space
def longest_palindrome_subseq_bottom_up(self, s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][n - 1]


# O(n^2) time || O(n) space
def longest_palindrome_subseq(self, s: str) -> int:
    n = len(s)
    dp, dp_prev = [0] * n, [0] * n
    for i in range(n - 1, -1, -1):
        dp[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[j] = dp_prev[j - 1] + 2
            else:
                dp[j] = max(dp_prev[j], dp[j - 1])
        dp, dp_prev = dp_prev, dp

    return dp_prev[-1]
