from typing import List


# O(n) time | O(1) space
def min_sub_array_len(self, target: int, nums: List[int]) -> int:
    i, res = 0, len(nums) + 1
    for j in range(len(nums)):
        target -= nums[j]
        while target <= 0:
            res = min(res, j - i + 1)
            target += nums[i]
            i += 1

    return res % (len(nums) + 1)
