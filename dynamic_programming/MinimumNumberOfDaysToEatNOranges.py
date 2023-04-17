from functools import lru_cache


# O(n) time || O(n) space
@lru_cache(None)
def min_days(self, n: int) -> int:
    if n <= 1:
        return n

    return 1 + min(n % 2 + min_days(self, n // 2), n % 3 + min_days(self, n // 3))
