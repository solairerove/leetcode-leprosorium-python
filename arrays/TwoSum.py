from typing import List


# O(n) time || O(n) space
def two_sum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return [dic[target - num], i]
        dic[num] = i
