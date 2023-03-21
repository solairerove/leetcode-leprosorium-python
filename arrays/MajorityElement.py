from collections import Counter
from typing import List


# O(n * log(n)) time || O(1) space
def majority_element_sort(self, nums: List[int]) -> int:
    nums.sort()

    return nums[len(nums) // 2]


# O(n) time || O(n) space
def majority_element_hm(self, nums: List[int]) -> int:
    cnt = Counter(nums)

    return max(cnt.keys(), key=cnt.get)
