# O(n) time || O(1) space
from functools import lru_cache


# O(n) time || O(1) space
def fib(self, n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


# O(n) time || O(n) space
def fib_top_down(self, n: int) -> int:
    @lru_cache(n)
    def dp(i):
        if i == 0:
            return 0

        if i == 1:
            return 1

        return dp(i - 1) + dp(i - 2)

    return dp(n)
