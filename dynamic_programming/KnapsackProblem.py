from typing import List


# O(2^n) time || O(n) space
def knapsack_recursion(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    # def helper(ith: int, free_space: int) -> int:
    #     if ith >= n - 1 or free_space < 0:
    #         return 0
    #
    #     if weights[ith + 1] > free_space:
    #         return 0
    #
    #     return max(
    #         helper(ith + 1, free_space),
    #         helper(ith, free_space - weights[ith + 1]) + items[ith + 1]
    #     )
    #
    # return helper(-1, capacity)
    #
    if n == 0 or capacity == 0 or weights[n - 1] > capacity:
        return 0

    return max(
        knapsack_recursion(self, items, weights, n - 1, capacity),
        items[n - 1] + knapsack_recursion(self, items, weights, n - 1, capacity - weights[n - 1]),
    )
