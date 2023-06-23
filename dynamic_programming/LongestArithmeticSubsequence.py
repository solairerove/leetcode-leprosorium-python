from typing import List


# O(n^2) time || O(n^2) space
def longest_arith_seq_length(self, nums: List[int]) -> int:
    dp = {}
    for i in range(len(nums)):
        for j in range(0, i):
            diff = nums[i] - nums[j]
            dp[(i, diff)] = dp.get((j, diff), 1) + 1

    return max(dp.values())
