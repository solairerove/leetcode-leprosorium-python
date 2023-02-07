from typing import List


# O(2^n) time || O(n) space
def knapsack_recursion(self, items: List[int], weights: List[int], n: int, capacity: int) -> int:
    if n == 0 or capacity == 0 or weights[n - 1] > capacity:
        return 0

    return max(
        knapsack_recursion(self, items, weights, n - 1, capacity),
        items[n - 1] + knapsack_recursion(self, items, weights, n - 1, capacity - weights[n - 1]),
    )
