from functools import lru_cache


# O(m * n) time || O(m * n) space
def unique_paths_top_down(self, m: int, n: int) -> int:
    @lru_cache(None)
    def dp(i, j):
        if i < 1 or j < 1:
            return 0

        if i == 1 and j == 1:
            return 1

        return dp(i, j - 1) + dp(i - 1, j)

    return dp(m, n)


# O(m * n) time || O(n) space
def unique_paths_bottom_up(self, m: int, n: int) -> int:
    row = [1] * n
    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row

    return row[0]
