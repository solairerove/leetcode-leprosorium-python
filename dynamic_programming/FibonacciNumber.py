# O(n) time || O(1) space
from functools import lru_cache


def fib(self, n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


# O(n) time || O(n) space
@lru_cache(None)
def fib_rec(self, n: int) -> int:
    if n <= 1:
        return n

    return fib_rec(self, n - 1) + fib_rec(self, n - 2)
