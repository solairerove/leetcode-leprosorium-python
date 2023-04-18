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


# O(n) time || O(1) space
def trap_two_pointers(self, height: List[int]) -> int:
    if len(height) <= 2:
        return 0

    n = len(height)
    max_low, max_high = height[0], height[-1]
    low, high = 1, n - 2
    res = 0
    while low <= high:
        if max_low < max_high:
            if height[low] > max_low:
                max_low = height[low]
            else:
                res += max_low - height[low]
            low += 1
        else:
            if height[high] > max_high:
                max_high = height[high]
            else:
                res += max_high - height[high]
            high -= 1

    return res
