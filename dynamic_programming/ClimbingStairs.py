from functools import lru_cache


# O(n) time || O(1) space
def climb_stairs(self, n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = a + b, a

    return a


# O(n) time || O(n) space
def climb_stairs_rec_bottom_up(self, n: int) -> int:
    @lru_cache(None)
    def helper(ith: int) -> int:
        if ith > n:
            return 0

        if ith == n:
            return 1

        return helper(ith + 1) + helper(ith + 2)

    return helper(0)


# O(n) time || O(n) space
def climb_stairs_rec_top_down(self, n: int) -> int:
    @lru_cache(None)
    def helper(ith: int) -> int:
        if ith == 0:
            return 0
        if ith == 1:
            return 1

        return helper(ith - 1) + helper(ith - 2)

    return helper(n + 1)
