# O(n) time || O(1) space
from functools import lru_cache


def fib(self, n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


# O(n) time || O(n) space
def fib_rec(self, n: int) -> int:
    @lru_cache(None)
    def helper(ith: int) -> int:
        if ith == 0:
            return 0
        if ith == 1:
            return 1

        return helper(ith - 1) + helper(ith - 2)

    return helper(n)
