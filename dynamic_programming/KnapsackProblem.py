from typing import List


# O(2^n) time || O(n) space
def knapsack_recursion(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack_recursion(self, items, weights, n - 1, capacity)
    else:
        return max(
            items[n - 1] + knapsack_recursion(self, items, weights, n - 1, capacity - weights[n - 1]),
            knapsack_recursion(self, items, weights, n - 1, capacity)
        )
