from typing import List


# O(n) time || O(n) space
def contains_duplicate(self, nums: List[int]) -> bool:
    return len(nums) != len((set(nums)))
