from typing import List


# TODO: two pointers

# O(n) time || O(1) space
def max_area(self, height: List[int]) -> int:
    res, low, high = 0, 0, len(height) - 1
    while low < high:
        res = max(res, (high - low) * (min(height[low], height[high])))
        if height[low] <= height[high]:
            low += 1
        else:
            high -= 1

    return res
