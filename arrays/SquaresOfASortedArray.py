from typing import List


# O(n) time || O(n) space
def sorted_squares(self, nums: List[int]) -> List[int]:
    return []


# O(n * log(n)) time || O(n) space
def sorted_squares_sorting(self, nums: List[int]) -> List[int]:
    return sorted(x * x for x in nums)
