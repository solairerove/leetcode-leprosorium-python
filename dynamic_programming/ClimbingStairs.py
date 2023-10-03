from functools import lru_cache


# O(n) time || O(1) space
def climb_stairs(self, n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = a + b, a

    return a


# O(n) time || O(n) space
def climb_stairs_top_down(self, n: int) -> int:
    @lru_cache(None)
    def dp(i):
        if i > n:
            return 0

        if i == n:
            return 1

        return dp(i + 1) + dp(i + 2)

    return dp(0)


# O(n) time || O(n) space
def climb_stairs_bottom_up(self, n: int) -> int:
    if n < 3:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]
