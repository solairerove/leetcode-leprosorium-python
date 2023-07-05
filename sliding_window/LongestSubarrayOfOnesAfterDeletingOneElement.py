from typing import List


# O(n) time | O(1) space
def longest_subarray(self, nums: List[int]) -> int:
    k, i, j = 1, 0, 0
    for j in range(len(nums)):
        k -= nums[j] == 0
        if k < 0:
            k += nums[i] == 0
            i += 1

    return j - i
