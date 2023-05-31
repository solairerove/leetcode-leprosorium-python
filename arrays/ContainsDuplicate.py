from typing import List


# just compare lengths of array and set
# also we can sort and check if we have value that appears at least twice

# O(n) time || O(n) space
def contains_duplicate(self, nums: List[int]) -> bool:
    return len(nums) != len((set(nums)))
