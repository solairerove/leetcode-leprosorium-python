from typing import List


# O(n) time || O(1) space
def two_sum(self, nums: List[int], target: int) -> List[int]:
    if len(nums) == 2:
        return [1, 2]

    low, high = 0, len(nums) - 1
    while low < high:
        potential_sum = nums[low] + nums[high]

        if potential_sum < target:
            low += 1
        elif potential_sum > target:
            high -= 1
        else:
            return [low + 1, high + 1]

    return [-1, -1]
