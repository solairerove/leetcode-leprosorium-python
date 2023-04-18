from typing import List


# O(n) time || O(n) space
def trap(self, height: List[int]) -> int:
    n = len(height)
    max_low, max_high = [0] * n, [0] * n

    for i in range(1, n):
        max_low[i] = max(height[i - 1], max_low[i - 1])

    for i in range(n - 2, -1, -1):
        max_high[i] = max(height[i + 1], max_high[i + 1])

    res = 0
    for i in range(n):
        level = min(max_low[i], max_high[i])
        if level >= height[i]:
            res += level - height[i]

    return res
