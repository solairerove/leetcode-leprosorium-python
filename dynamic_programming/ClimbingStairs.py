from functools import lru_cache


# O(n) time || O(1) space
def climb_stairs(self, n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = a + b, a

    return a


# O(n) time || O(1) space
def climb_stairs_rec(self, n: int) -> int:
    @lru_cache(None)
    def helper(s) -> int:
        if s > n:
            return 0

        if s == n:
            return 1

        return helper(s + 1) + helper(s + 2)

    return helper(0)
