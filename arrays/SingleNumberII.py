from typing import List


# O(n) time || O(1) space
def single_number(self, nums: List[int]) -> int:
    ones = twos = 0
    for num in nums:
        ones ^= (num & ~twos)
        twos ^= (num & ~ones)

    return ones
