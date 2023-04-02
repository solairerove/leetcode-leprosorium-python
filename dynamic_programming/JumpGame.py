from typing import List


# O(n) time || O(1) space
def can_jump(self, nums: List[int]) -> bool:
    high = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= high:
            high = i

    return high == 0
