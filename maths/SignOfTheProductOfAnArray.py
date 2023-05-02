from typing import List


# O(n) time || O(1) space
def array_sign(self, nums: List[int]) -> int:
    res = 1
    for num in nums:
        if num == 0:
            return 0

        if num < 0:
            res *= -1

    return res
