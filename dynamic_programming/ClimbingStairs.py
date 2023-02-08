from functools import lru_cache


# O(n) time || O(1) space
def climb_stairs(self, n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = a + b, a

    return a


# O(n) time || O(n) space
def climb_stairs_rec(self, n: int) -> int:
    @lru_cache(None)
    def dp(i: int) -> int:
        if i <= 2:
            return i

        return dp(i - 1) + dp(i - 2)

    return dp(n)
