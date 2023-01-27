from collections import Counter
from typing import List


# O(n) time || O(n) space
def find_duplicates_hs(self, nums: List[int]) -> List[int]:
    d = Counter(nums)
    return [k for k, v in d.items() if v == 2]


# O(n) time || O(1) space
def find_duplicates(self, nums: List[int]) -> List[int]:
    res = []
    for n in nums:
        if nums[abs(n) - 1] < 0:
            res.append(abs(n))
        else:
            nums[abs(n) - 1] *= -1

    return res
