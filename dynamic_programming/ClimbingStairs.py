from functools import lru_cache


# O(n) time || O(1) space
def climb_stairs(self, n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = a + b, a

    return a


# O(n) time || O(n) space
def climb_stairs_top_down(self, n: int) -> int:
    @lru_cache(n)
    def dp(i):
        if i == 0:
            return 0

        if i == 1:
            return 1

        return dp(i - 1) + dp(i - 2)

    return dp(n + 1)


# O(n) time || O(n) space
def climb_stairs_bottom_up(self, n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
