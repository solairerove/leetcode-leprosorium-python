from typing import List


# it's just math formula

# O(n) time || O(1) space
def missing_number(self, nums: List[int]) -> int:
    n = len(nums)

    return n * (n + 1) // 2 - sum(nums)
