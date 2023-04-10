from functools import lru_cache


# O(n) time || O(1) space
def tribonacci(self, n: int) -> int:
    a, b, c = 1, 0, 0
    for _ in range(n):
        a, b, c = b, c, a + b + c

    return c


# O(n) time || O(1) space
def tribonacci_from_smart_guy(self, n: int) -> int:
    dp = [0, 1, 1]
    for i in range(3, n + 1):
        dp[i % 3] = sum(dp)

    return dp[n % 3]


# O(n) time || O(n) space
def tribonacci_top_down(self, n: int) -> int:
    @lru_cache(None)
    def dp(i):
        if i == 0:
            return 0

        if i == 1 or i == 2:
            return 1

        return dp(i - 1) + dp(i - 2) + dp(i - 3)

    return dp(n)
