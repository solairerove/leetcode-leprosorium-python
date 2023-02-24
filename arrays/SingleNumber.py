from typing import List


# O(n) time || O(1) space
def single_number(self, nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i

    return a
