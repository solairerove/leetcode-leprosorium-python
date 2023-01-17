from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    return max(nums[0], helper(self, nums[1:]), helper(self, nums[:-1]))


def helper(self, nums: List[int]) -> int:
    rob1 = rob2 = 0
    for n in nums:
        tmp = max(rob1 + n, rob2)
        rob1, rob2 = rob2, tmp

    return rob2
