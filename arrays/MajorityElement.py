from collections import Counter
from typing import List


# O(n) time || O(1) space
def majority_element_boyer_moore_voting(self, nums: List[int]) -> int:
    cnt, res = 0, None
    for num in nums:
        if cnt == 0:
            res = num
        cnt += (1 if num == res else -1)

    return res


# O(n * log(n)) time || O(1) space
def majority_element_sort(self, nums: List[int]) -> int:
    nums.sort()

    return nums[len(nums) // 2]


# O(n) time || O(n) space
def majority_element_hm(self, nums: List[int]) -> int:
    cnt = Counter(nums)

    return max(cnt.keys(), key=cnt.get)
