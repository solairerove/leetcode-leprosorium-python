from typing import List


# O(n) time || O(1) space
def missing_number(self, nums: List[int]) -> int:
    n = len(nums)

    return n * (n + 1) // 2 - sum(nums)
