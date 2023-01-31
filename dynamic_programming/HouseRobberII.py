from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    def helper(arr: List[int]) -> int:
        rob1 = rob2 = 0
        for n in arr:
            rob1, rob2 = rob2, max(rob1 + n, rob2)

        return rob2

    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
