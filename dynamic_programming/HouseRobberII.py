from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    def classic_rob(arr: List[int]) -> int:
        prev = curr = 0
        for n in arr:
            prev, curr = curr, max(curr, prev + n)

        return curr

    return max(nums[0], classic_rob(nums[1:]), classic_rob(nums[:-1]))


# O(n) time || O(n) space
def rob_top_down(self, nums: List[int]) -> int:
    def classic_rob(arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            if i >= len(arr):
                return 0

            return max(dp(i + 1), dp(i + 2) + arr[i])

        return dp(0)

    return max(nums[0], classic_rob(nums[1:]), classic_rob(nums[:-1]))
