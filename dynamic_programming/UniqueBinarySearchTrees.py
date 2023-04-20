from functools import lru_cache


# O(n ^ 2) time || O(n) space
@lru_cache(None)
def num_trees_top_down(self, n: int) -> int:
    if n <= 1:
        return 1

    return sum(num_trees_top_down(self, i - 1) * num_trees_top_down(self, n - i) for i in range(1, n + 1))


# O(n ^ 2) time || O(n) space
def num_trees_bottom_up(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[-1]
