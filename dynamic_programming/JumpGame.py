from typing import List


# O(n) time || O(1) space
def can_jump(self, nums: List[int]) -> bool:
    high = 0
    for i, n in enumerate(nums):
        if i > high:
            return False
        high = max(high, i + n)

    return True
