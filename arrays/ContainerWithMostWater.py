from typing import List

# TODO: two pointers

# O(n) time || O(1) space
def max_area(self, height: List[int]) -> int:
    res = 0
    low, high = 0, len(height) - 1
    while low < high:
        curr_width = high - low
        curr_height = min(height[low], height[high])
        res = max(res, curr_width * curr_height)

        if height[low] <= height[high]:
            low += 1
        else:
            high -= 1

    return res
