from functools import lru_cache


# O(n ^ 2) time || O(n) space
@lru_cache(None)
def num_trees_top_down(self, n: int) -> int:
    if n <= 1:
        return 1

    return sum(num_trees_top_down(self, i - 1) * num_trees_top_down(self, n - i) for i in range(1, n + 1))
